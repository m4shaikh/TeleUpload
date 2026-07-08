# 🚀 Telegram Video Uploader

A fast, clean, and extensible **Telegram video uploader** built with **Python** and **Telethon**.

This project automatically uploads videos from a directory to a Telegram channel while displaying real-time upload progress, preserving video metadata, and generating thumbnails for a better viewing experience.

Designed with modularity in mind, it also serves as the foundation for a future **high-performance MTProto uploader** with parallel chunk uploads similar to Telegram Desktop.

---

## ✨ Features

* 📂 Upload every video from a directory
* 🎬 Automatic video metadata extraction
* 🖼️ Automatic thumbnail generation
* 📺 Streaming-enabled uploads
* 📊 Live upload progress
* 🔢 Upload files in numeric order
* 🧹 Automatic cleanup of generated thumbnails
* 🏗️ Clean and modular codebase

---

## 📁 Project Structure

```text
telegram_uploader/
│
├── main.py                 # Entry point
├── uploader.py             # Upload manager
├── progress_callback.py    # Upload progress
├── utils.py                # File, metadata & thumbnail utilities
├── config.py               # API credentials
└── README.md
```

---

## 📦 Requirements

* Python 3.10+
* FFmpeg (includes ffprobe)
* Telegram API credentials

Python packages:

```bash
pip install telethon
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/telegram-video-uploader.git

cd telegram-video-uploader
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install **FFmpeg** and ensure both `ffmpeg` and `ffprobe` are available in your system PATH.

---

## 🔑 Configuration

Create a `config.py` file.

```python
API_ID = YOUR_API_ID
API_HASH = "YOUR_API_HASH"

CHANNEL = "your_channel_username_or_id"
```

You can obtain your API credentials from:

https://my.telegram.org

---

## ▶️ Usage

```bash
python main.py "/path/to/videos"
```

Example:

```bash
python main.py "D:/Movies"
```

---

## 📹 Supported Formats

* MP4
* MKV
* AVI
* MOV
* WEBM

---

## 🛠️ How It Works

1. Scans the provided directory.
2. Sorts videos numerically.
3. Extracts video metadata.
4. Generates a thumbnail using FFmpeg.
5. Uploads the video with:

   * Streaming support
   * Duration
   * Resolution
   * Thumbnail
6. Displays upload progress.
7. Removes the temporary thumbnail.

---

## 📈 Roadmap

* [ ] Parallel MTProto uploads
* [ ] Custom chunk scheduler
* [ ] Multiple upload workers
* [ ] Resume interrupted uploads
* [ ] Automatic retries
* [ ] Upload queue management
* [ ] Configurable thumbnail timestamp
* [ ] CLI configuration options
* [ ] Upload statistics
* [ ] Telegram Desktop–like upload performance

---

## 🤝 Contributing

Contributions, feature requests, and bug reports are welcome.

Feel free to open an issue or submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Future Vision

The long-term goal of this project is to evolve beyond Telethon's built-in `send_file()` implementation and build a custom **high-performance MTProto uploader** from scratch. The aim is to implement parallel chunk uploads, intelligent scheduling, retry mechanisms, and upload optimizations comparable to Telegram Desktop while keeping the codebase clean, educational, and open source.
