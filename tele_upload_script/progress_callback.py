import time


class UploadProgress:

    def __init__(self, filename):
        self.filename = filename
        self.start = time.time()
        self.last_update = 0

    def update(self, current, total):

        now = time.time()

        if now - self.last_update < 0.5:
            return

        self.last_update = now

        elapsed = max(now - self.start, 0.001)

        speed = current / elapsed

        percent = current / total * 100
        
        eta = (total - current) / speed if speed else 0

        bar_length = 30

        filled = int(percent / 100 * bar_length)

        bar = "█" * filled + "░" * (bar_length - filled)

        print(
            f"\r[{bar}] "
            f"{percent:6.2f}% "
            f"| {current/1024/1024:7.1f} MB"
            f"/{total/1024/1024:.1f} MB "
            f"| {speed/1024/1024:6.2f} MB/s "
            f"| ETA {eta:5.0f}s",
            end="",
            flush=True
        )   