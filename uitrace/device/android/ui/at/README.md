### 修复adb路径
    at/core/adbwrap.py
    def get_adb()
    def run_cmd() 修改mac和win使用同一个popen，传入字符串，不进行分割
    
    at/core/javadriver.py
    def _run_app_server 修改mac和win使用同一个popen，传入字符串，不进行分割

### 修复bin安装文件路径
    at/core/config.py
    AT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    改成
    AT_ROOT = os.path.join(proj_env.lib_dir, "device", "android", "ui", "at", "at")

### 全局修改logger为logging.getLogger("at")

### 保存log到文件
    at/__init__.py at line 31 def save_log
