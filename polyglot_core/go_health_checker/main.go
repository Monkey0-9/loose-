package main

import (
	"encoding/json"
	"fmt"
	"os"
	"path/filepath"
	"sync"
	"time"
)

type AgentStatus struct {
	Name     string `json:"name"`
	Category string `json:"category"`
	Status   string `json:"status"`
}

type HealthReport struct {
	Timestamp   string                 `json:"timestamp"`
	TotalAgents int                    `json:"total_agents"`
	Categories  map[string]interface{} `json:"categories"`
	Agents      []AgentStatus          `json:"agents"`
}

var CATEGORIES = []string{
	"core_modules", "utility_modules", "mcp_connectors",
	"memory_persistence", "rag_infrastructure", "advanced_engines",
}

func checkAgent(cat, name string, wg *sync.WaitGroup, results chan<- AgentStatus) {
	defer wg.Done()

	// High-fidelity Go simulation of health checking
	status := "HEALTHY"
	entryPoints := []string{"main.py", "app.py", "agent.py", "index.ts", "monitor.ts"}
	found := false
	for _, ep := range entryPoints {
		if _, err := os.Stat(filepath.Join(cat, name, ep)); err == nil {
			found = true
			break
		}
	}

	if !found {
		status = "ERROR: Missing Entry Point"
	}

	results <- AgentStatus{
		Name:     name,
		Category: cat,
		Status:   status,
	}
}

func logEvent(level, message string) {
	file, _ := os.OpenFile("../../telemetry.json", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	defer file.Close()
	event := fmt.Sprintf(`{"timestamp":"%s","module":"go_auditor","level":"%s","message":"%s"}`+"\n",
		time.Now().Format(time.RFC3339), level, message)
	file.WriteString(event)
}

func main() {
	fmt.Println("🚀 Loose AI - Ultra-Fast Go Health Auditor")
	fmt.Println("Scanning ecosystem in parallel...")

	var wg sync.WaitGroup
	results := make(chan AgentStatus, 1000)
	total := 0

	logEvent("INFO", "Starting parallel health audit...")
	start := time.Now()

	for _, cat := range CATEGORIES {
		entries, err := os.ReadDir(cat)
		if err != nil {
			continue
		}

		for _, entry := range entries {
			if entry.IsDir() && entry.Name()[0] != '_' {
				wg.Add(1)
				total++
				go checkAgent(cat, entry.Name(), &wg, results)
			}
		}
	}

	go func() {
		wg.Wait()
		close(results)
	}()

	report := HealthReport{
		Timestamp:   time.Now().Format(time.RFC3339),
		TotalAgents: total,
		Categories:  make(map[string]interface{}),
		Agents:      []AgentStatus{},
	}

	for status := range results {
		report.Agents = append(report.Agents, status)
	}

	duration := time.Since(start)
	fmt.Printf("\n✅ Scanned %d agents in %v\n", total, duration)

	file, _ := json.MarshalIndent(report, "", "  ")
	_ = os.WriteFile("go_health_report.json", file, 0644)
	fmt.Println("Report saved to go_health_report.json")
}
