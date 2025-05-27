from agent.orchestrator import run_weekly_report, run_single_analysis
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "weekly":
            run_weekly_report()
        elif sys.argv[1] == "single" and len(sys.argv) > 2:
            run_single_analysis(sys.argv[2])
        else:
            print("Använd: python main.py weekly | python main.py single TICKER")
    else:
        print("Välj ett kommando.")