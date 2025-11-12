# ⚙️ HPC Forge 🔥

**HPC Forge** is a powerful, lightweight CLI toolkit designed to simplify everyday tasks for developers, researchers, and students working in **High-Performance Computing (HPC)** environments.  

It helps you **generate optimized Makefiles**, **create SLURM job scripts**, and **apply pre-configured templates** for clusters like **Deucalion**, **SeARCH**, or your own local HPC setup — all interactively, from the terminal.

---


![Demo](https://github.com/diogocsilva12/hpcforge/blob/1ec662a78adbb54975283038d92b89843e55601f/WindowsTerminal_GoKppokiMS.png?raw=true)

## 🚀 Features

| Feature | Description |
|----------|-------------|
| 🧱 **Makefile Generator** | Interactive creation of Makefiles with auto-optimized compiler flags for `gcc`, `clang`, and `scorep` |
| 🧩 **SLURM Job Script Generator** | Quickly build `.slurm` job scripts with dynamic runtime estimates |
| 🌌 **Deucalion Mode** | Instantly load tuned parameters for the Deucalion cluster (fully editable) |
| 📂 **Template Viewer** | Browse, preview, or apply built-in templates with syntax highlighting |
| ⚙️ **Interactive Menu System** | Clean, arrow-key-driven interface powered by `questionary` |
| 🧠 **Smart Defaults** | Context-aware recommendations and examples for each field |
| 🧰 **Extensible Design** | Modular architecture for future commands like `doctor`, `deploy`, or `benchmark` |
| 🛠 **Roadmap** | Continuous improvement toward a full HPC automation toolkit |

---

## 🧑‍💻 Installation

### 📦 From PyPI (recommended)
```bash
pip install hpcforge-cli
hpctools        
```

### From Source
```bash
git clone https://github.com/diogocsilva12/hpcforge.git
cd hpcforge
pip install -e .

hpctools
```

### Usage
Run the main CLI menu:
```bash
hpctools
``` 

```bash
hpctools make
hpctools slurm
hpctools slurm
```



### Contributing
Contributions are welcome!
1. Fork the repository
2. Create a new branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

### License
MIT License. See `LICENSE` file for details.

### Links
- **Repository:** [github.com/diogocsilva12/hpcforge](https://github.com/diogocsilva12/hpcforge)
- **Changelog:** See `CHANGELOG.md` for detailed version history and upcoming features.
- PyPI Package: [pypi.org/project/hpcforge-cli](https://pypi.org/project/hpcforge-cli)
- Issues & Discussions: [github.com/diogocsilva12/hpcforge/issues](https://github.com/diogocsilva12/hpcforge/issues)

