import * as fs from 'fs';
import * as path from 'path';

interface AgentInfo {
    name: string;
    category: string;
    isProductionReady: boolean;
}

const CATEGORIES = [
    "Core_ai_agents", "simple_ai_agents", "mcp_ai_agents",
    "memory_agents", "rag_apps", "advance_ai_agents"
];

function scanEcosystem(): void {
    console.log("🟦 Loose AI - TypeScript Ecosystem Monitor");
    const agents: AgentInfo[] = [];

    CATEGORIES.forEach(cat => {
        const catPath = path.join(process.cwd(), cat);
        if (fs.existsSync(catPath)) {
            const dirs = fs.readdirSync(catPath);
            dirs.forEach(dir => {
                const agentPath = path.join(catPath, dir);
                if (fs.statSync(agentPath).isDirectory() && !dir.startsWith("__")) {
                    const hasEnv = fs.existsSync(path.join(agentPath, ".env.Integration"));
                    agents.push({
                        name: dir,
                        category: cat,
                        isProductionReady: hasEnv
                    });
                }
            });
        }
    });

    console.table(agents.slice(0, 10));
    console.log(`\nTotal Agents Monitored: ${agents.length}`);
}

scanEcosystem();
