import os
from dotenv import load_dotenv, find_dotenv
from openai import AzureOpenAI
import nflreadpy as nfl
from rich.console import Console
from rich.table import Table

console = Console()
load_dotenv(find_dotenv(), override=True)

API_KEY = os.getenv("AZURE_OPENAI_API_KEY", "").strip()
ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT", "").strip().rstrip("/")
DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "").strip()
API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2024-08-01-preview").strip()

if not all([API_KEY, ENDPOINT, DEPLOYMENT]):
    console.print("[bold red]❌ Config Error: Check your .env for missing values.[/]")
    exit(1)

client = AzureOpenAI(
    api_key=API_KEY,
    azure_endpoint=ENDPOINT,
    api_version=API_VERSION
)

def run_scout_report():
    table = Table(title="🏈 Super Bowl LX Scouting War Room")
    table.add_column("Player", style="cyan")
    table.add_column("2025 Avg", style="magenta")
    table.add_column("Market Line", style="yellow")
    table.add_column("AI Verdict", style="green")

    with console.status("[bold green]Harvesting 2025 NFLverse Intel..."):
        try:
            # High-performance 2025 data ingestion
            weekly_data = nfl.load_player_stats([2025]).to_pandas()
        except Exception as e:
            console.print(f"[red]NFL Data Error: {e}[/]")
            return

    # Updated names to match the nflverse 'player_name' column exactly
    targets = [
        {"name": "Drake Maye", "line": 228.5, "type": "passing_yards"},
        {"name": "Kenneth Walker", "line": 74.5, "type": "rushing_yards"}
    ]

    for t in targets:
        try:
            # 1. Attempt to pull from the library first
            player_data = weekly_data[weekly_data['player_name'].str.contains(t['name'], case=False, na=False)]
            avg = player_data[t['type']].mean() if not player_data.empty else 0
            
            # --- START MANUAL INJECTION BLOCK ---
            # Verified 2025 stats to bypass library lag
            manual_stats = {
                "Drake Maye": 258.5,
                "Kenneth Walker": 60.4
            }

            if avg == 0 and t['name'] in manual_stats:
                avg = manual_stats[t['name']]
                console.print(f"[yellow]⚠️ Data Sync Delay: Injecting verified 2025 stats for {t['name']}[/]")
           
            response = client.chat.completions.create(
                model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
                messages=[{"role": "user", "content": f"Scout {t['name']}: {avg:.1f} avg. Line: {t['line']}. Over/Under?"}]
            )
            
            verdict = response.choices[0].message.content.strip()
            table.add_row(t['name'], f"{avg:.1f} Yds", str(t['line']), verdict)
        
        except Exception as e:
            console.print(f"[red]Scouting Error for {t['name']}: {e}[/]")

    console.print(table)

if __name__ == "__main__":
    run_scout_report()