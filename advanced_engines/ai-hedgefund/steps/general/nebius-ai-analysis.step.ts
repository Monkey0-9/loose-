import { EventConfig, Handlers } from 'motia';
import { z } from 'zod';
import { ServiceFactory } from '../../services/utils/ServiceFactory';
import { AnalysisInput } from '../../services/types';


export const config: EventConfig = {
  type: 'event',
  name: 'Loose-ai-analysis',
  description: 'Analyzes financial data using Loose AI Engine and triggers parallel specialized analyses',
  subscribes: ['response.completed'],
  emits: ['parallel.analyses.started'],
  input: z.object({
    query: z.string().optional(),
    timestamp: z.string(),
    response: z.any(),
    error: z.string().optional()
  }),
  flows: ['aihedgefund-workflow']
};

export const handler: Handlers['Loose-ai-analysis'] = async (input, { logger, emit, state, traceId }) => {
  logger.info('Starting Loose AI Engine analysis and parallel specialized analyses', { traceId });
  
  try {
    if (!input.response) {
      logger.error('No response data provided', { traceId });
      
      await emit({
        topic: 'parallel.analyses.started',
        data: {
          query: input.query,
          timestamp: input.timestamp,
          response: input.response,
          analysisInput: null,
          generalAnalysis: null,
          traceId
        }
      });
      return;
    }
    
    const stateService = ServiceFactory.createStateService(state, traceId);
    
    const { query, response } = input;
    
    const analysisInput: AnalysisInput = {
      query: query || 'Unknown query',
      webResources: (response as any)?.webResources || [],
      financialData: (response as any)?.financialData || []
    };
    
    const LooseService = ServiceFactory.getLooseAIService();
    
    const generalAnalysis = await LooseService.performAnalysis(analysisInput);
    
    await stateService.set('ai.analysis', generalAnalysis);
    
    // Emit event to trigger parallel analyses
    await emit({
      topic: 'parallel.analyses.started',
      data: {
        query: input.query,
        timestamp: input.timestamp,
        response: input.response,
        analysisInput,
        generalAnalysis,
        traceId
      }
    });
    
  } catch (error) {
    logger.error('Loose AI Engine analysis failed', { error });
    await emit({
      topic: 'parallel.analyses.started',
      data: {
        query: input.query,
        timestamp: input.timestamp,
        response: input.response,
        analysisInput: null,
        generalAnalysis: null,
        traceId
      }
    });
  }
}; 