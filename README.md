# TUI File Explorer

A terminal-based file explorer built with Python and Textual, providing a fast and intuitive way to navigate your filesystem directly from the command line.

## Features

- 📁 Browse directories and files in a clean TUI interface
- ⌨️ Keyboard-driven navigation for efficiency
- 🐧 Guaranteed Linux support (Windows/macOS compatibility in progress)
- 🎨 Modern terminal UI with Textual library
- ⚡ Lightweight and fast

## Screenshots

*Coming soon*

## Requirements

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/tui-file-explorer.git
cd tui-file-explorer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the file explorer:
```bash
python main.py
```

### Keyboard Shortcuts

*To be documented as features are implemented*

- `↑/↓` - Navigate through files and directories
- `Enter` - Open directory or file
- `q` - Quit application
- `Backspace` - Go to parent directory

## Platform Support

| Platform | Status |
|----------|--------|
| Linux    | ✅ Supported |
| macOS    | 🚧 Experimental |
| Windows  | 🚧 Experimental |

**Note:** This project is primarily developed and tested on Linux. While it may work on other platforms, full compatibility is not guaranteed at this time.

## Development

### Project Structure

```
tui-file-explorer/
├── explorer.py       # Main application file
├── requirements.txt  # Python dependencies
├── README.md        # This file
└── LICENSE          # Project license
```

### Contributing

Contributions are welcome! If you'd like to help improve cross-platform support or add new features:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Roadmap

- [ ] File operations (copy, move, delete)
- [ ] File search functionality
- [ ] File preview
- [ ] Better cross-platform support
- [ ] Configuration file support
- [ ] Themes and customization

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Textual](https://textual.textualize.io/) by Textualize
- Inspired by classic file managers like Midnight Commander and ranger

## Known Issues

- Cross-platform compatibility not fully tested
- Some special characters in filenames may not display correctly

## Contact

For questions or feedback, please open an issue on GitHub.

---

**Note:** This is an active development project. Features and compatibility may change.
