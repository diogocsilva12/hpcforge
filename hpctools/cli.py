import sys
import os
import click
import questionary
from rich.console import Console
from rich.syntax import Syntax

from hpctools.makegen import generate_makefile
from hpctools.slurmgen import generate_slurm
from hpctools.utils import load_template
from hpctools.header import print_header


console = Console()


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """hpctools - HPC automation toolkit (Makefile + SLURM + Benchmarking)"""
    print_header()

    # Ask if user wants Deucalion mode globally
    ctx.obj = {}
    ctx.obj["deucalion_mode"] = questionary.confirm(
        "Enable Deucalion mode (cluster defaults)?"
    ).ask()

    # If no subcommand was provided → show menu
    if ctx.invoked_subcommand is None:
        while True:
            choice = questionary.select(
                "Select an option:",
                choices=[
                    "Generate Makefile",
                    "Generate SLURM job script",
                    "Generate both (Makefile + SLURM)",
                    "📂 View available templates",
                    "Exit",
                ],
            ).ask()

            if choice.startswith("Generate Makefile"):
                ctx.invoke(make)
            elif choice.startswith("Generate SLURM job script"):
                ctx.invoke(slurm, deucalion_mode=ctx.obj["deucalion_mode"])
            elif choice.startswith("Generate both"):
                ctx.invoke(all, deucalion_mode=ctx.obj["deucalion_mode"])
            elif choice.startswith("📂 View available templates"):
                ctx.invoke(templates)
            else:
                console.print("\n[bold cyan]👋 Exiting HPC Tools. Goodbye![/bold cyan]\n")
                sys.exit(0)


# ------------------- MAKE -------------------
@cli.command()
@click.option("--template", is_flag=True, help="Use a Makefile template instead of manual input.")
def make(template):
    """Create a Makefile (interactive or template-based)."""
    if not template:
        template = questionary.confirm("Generate from template?").ask()

    console.print("\n[bold cyan]🛠  Makefile Configuration[/bold cyan]\n")

    if template:
        tpl = input("Template file (default: make_default.mk): ").strip() or "make_default.mk"
        compiler = questionary.text("Compiler (e.g. gcc, scorep gcc, clang) [gcc]:").ask() or "gcc"
        flags = questionary.text("Compilation flags [-O2 -Wall]:").ask() or "-O2 -Wall"
        ldflags = questionary.text("Linker flags (e.g. -lm -pthread) [-lm]:").ask() or "-lm"
        src = questionary.text("Source files (space-separated) [main.c]:").ask() or "main.c"
        output = questionary.text("Output executable [a.out]:").ask() or "a.out"
        generate_makefile(
            compiler, flags, ldflags, src, output,
            use_template=True, template_name=tpl
        )
    else:
        compiler = questionary.text("Compiler (e.g. scorep gcc, clang) [scorep gcc]:").ask() or "scorep gcc"
        flags = questionary.text("Compilation flags [-Ofast -g -std=c99 -pedantic -Wall]:").ask() or "-Ofast -g -std=c99 -pedantic -Wall"
        ldflags = questionary.text("Linker flags [-lm]:").ask() or "-lm"
        src = questionary.text("Source files (.c) [main.c]:").ask() or "main.c"
        output = questionary.text("Output executable [a.out]:").ask() or "a.out"
        generate_makefile(compiler, flags, ldflags, src, output)

    console.print("[green]✅ Makefile successfully created![/green]")


# ------------------- SLURM -------------------
@cli.command()
@click.option("--template", is_flag=True, help="Use a SLURM template instead of manual input.")
@click.option("--deucalion-mode", is_flag=True, help="Activate Deucalion cluster defaults.")
def slurm(template, deucalion_mode):
    """Create a SLURM job script (interactive or template-based)."""
    if not template:
        template = questionary.confirm("Generate from template?").ask()

    console.print("\n[bold cyan]🚀 SLURM Job Configuration[/bold cyan]\n")

    # Deucalion mode: prefill default but still editable
    if deucalion_mode:
        console.print("[bold cyan]🌌 Deucalion mode enabled — preloading cluster defaults.[/bold cyan]")
        default_account = "f202500010hpcvlabuminhoa"
    else:
        default_account = ""

    account = questionary.text(
        f"SLURM account [{default_account or 'none'}]:",
        default=default_account
    ).ask() or default_account

    partition = questionary.text(
        "Partition (e.g. normal-arm, debug, gpu) [normal-arm]:",
        default="normal-arm"
    ).ask() or "normal-arm"

    time = questionary.text(
        "Time limit (hh:mm:ss) [00:35:00]:",
        default="00:35:00"
    ).ask() or "00:35:00"

    nodes = questionary.text("Number of nodes [1]:", default="1").ask() or "1"
    ntasks = questionary.text("Tasks per job [1]:", default="1").ask() or "1"
    cpus = questionary.text("CPUs per task [48]:", default="48").ask() or "48"
    exe = questionary.text("Executable path [./zpic]:", default="./zpic").ask() or "./zpic"
    runs = questionary.text("Number of runs [5]:", default="5").ask() or "5"

    if template:
        tpl = questionary.text("Template file (default: slurm_default.sh):", default="slurm_default.sh").ask() or "slurm_default.sh"
        generate_slurm(
            account, partition, time, nodes, ntasks, cpus, exe, runs,
            use_template=True, template_name=tpl
        )
    else:
        generate_slurm(account, partition, time, nodes, ntasks, cpus, exe, runs)

    console.print("[green]✅ SLURM job script successfully created![/green]")


# ------------------- ALL -------------------
@cli.command()
@click.option("--deucalion-mode", is_flag=True, help="Activate Deucalion cluster defaults.")
@click.pass_context
def all(ctx, deucalion_mode):
    """Generate both Makefile and SLURM job script."""
    ctx.invoke(make)
    ctx.invoke(slurm, deucalion_mode=deucalion_mode)


# ------------------- TEMPLATES -------------------
@cli.command()
def templates():
    """List and preview available templates in hpctools/templates."""
    base_dir = os.path.join(os.path.dirname(__file__), "templates")
    if not os.path.exists(base_dir):
        console.print("[red] No templates directory found.[/red]")
        return

    files = [f for f in os.listdir(base_dir) if os.path.isfile(os.path.join(base_dir, f))]
    if not files:
        console.print("[yellow] No template files found in hpctools/templates/[/yellow]")
        return

    console.print("\n[bold cyan] Available Templates:[/bold cyan]\n")
    for i, f in enumerate(files, 1):
        console.print(f"  {i}) [green]{f}[/green]")

    choice = questionary.text("\nEnter the template number to preview (or press Enter to exit): ").ask()
    if not choice or not choice.isdigit() or int(choice) < 1 or int(choice) > len(files):
        console.print("\n[dim]Exiting template viewer.[/dim]")
        return

    template_file = files[int(choice) - 1]

    try:
        content = load_template(template_file)
        if template_file.endswith(".mk"):
            syntax = Syntax(content, "make", theme="monokai", line_numbers=True)
        elif template_file.endswith(".sh"):
            syntax = Syntax(content, "bash", theme="monokai", line_numbers=True)
        else:
            syntax = Syntax(content, "text", theme="monokai", line_numbers=True)

        console.print(f"\n[bold blue] Previewing:[/bold blue] {template_file}\n")
        console.print(syntax)
    except Exception as e:
        console.print(f"[red] Failed to load template:[/red] {e}")


if __name__ == "__main__":
    cli()
