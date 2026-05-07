import { FinanceDataService } from '../Loose-ai/FinanceDataService';
import { LooseAIService } from '../Loose-ai/LooseAIService';
import { WebSearchService } from './WebSearchService';
import { StateService, IStateOperations } from './StateService';
import { ConfigService } from './ConfigService';

export class ServiceFactory {
  private static financeDataService: FinanceDataService | undefined;
  private static webSearchService: WebSearchService | undefined;
  private static LooseAIService: LooseAIService | undefined;

  public static getFinanceDataService(configService?: ConfigService): FinanceDataService {
    if (!this.financeDataService) {
      this.financeDataService = new FinanceDataService(configService);
    }
    return this.financeDataService;
  }

  public static getWebSearchService(apiKey?: string, searchUrl?: string): WebSearchService {
    if (!this.webSearchService) {
      this.webSearchService = new WebSearchService(apiKey, searchUrl);
    }
    return this.webSearchService;
  }

  public static getLooseAIService(apiKey?: string, baseURL?: string, model?: string): LooseAIService {
    if (!this.LooseAIService) {
      this.LooseAIService = new LooseAIService(apiKey, baseURL, model);
    }
    return this.LooseAIService;
  }

  public static createStateService(state: IStateOperations, defaultScope: string): StateService {
    return new StateService(state, defaultScope);
  }

  public static reset(): void {
    this.financeDataService = undefined;
    this.webSearchService = undefined;
    this.LooseAIService = undefined;
  }
} 