basic_ansi = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "reset": "\033[0m"
}

reset = "\033[0m"

banner = r"""

▒█▀▀▀ ▒█▄░▒█ ▒█▀▀█ ▒█▀▀▀█ ▒█▀▀▄ ▒█▀▀▀ ▀▄▒▄▀ 
▒█▀▀▀ ▒█▒█▒█ ▒█░░░ ▒█░░▒█ ▒█░▒█ ▒█▀▀▀ ░▒█░░ 
▒█▄▄▄ ▒█░░▀█ ▒█▄▄█ ▒█▄▄▄█ ▒█▄▄▀ ▒█▄▄▄ ▄▀▒▀▄
"""

colors = [
    basic_ansi["red"],
    basic_ansi["yellow"],
    basic_ansi["green"],
    basic_ansi["cyan"],
    basic_ansi["blue"],
    basic_ansi["magenta"]
]
for i, line in enumerate(banner.splitlines()):
    print(colors[i % len(colors)] + line + reset)

bold_map = {
    'A': '𝗔', 'B': '𝗕', 'C': '𝗖', 'D': '𝗗', 'E': '𝗘', 'F': '𝗙', 'G': '𝗚', 'H': '𝗛', 'I': '𝗜', 'J': '𝗝',
    'K': '𝗞', 'L': '𝗟', 'M': '𝗠', 'N': '𝗡', 'O': '𝗢', 'P': '𝗣', 'Q': '𝗤', 'R': '𝗥', 'S': '𝗦', 'T': '𝗧',
    'U': '𝗨', 'V': '𝗩', 'W': '𝗪', 'X': '𝗫', 'Y': '𝗬', 'Z': '𝗭',
    'a': '𝗮', 'b': '𝗯', 'c': '𝗰', 'd': '𝗱', 'e': '𝗲', 'f': '𝗳', 'g': '𝗴', 'h': '𝗵', 'i': '𝗶', 'j': '𝗷',
    'k': '𝗸', 'l': '𝗹', 'm': '𝗺', 'n': '𝗻', 'o': '𝗼', 'p': '𝗽', 'q': '𝗾', 'r': '𝗿', 's': '𝘀', 't': '𝘁',
    'u': '𝘂', 'v': '𝘃', 'w': '𝘄', 'x': '𝘅', 'y': '𝘆', 'z': '𝘇',
    '0': '𝟬', '1': '𝟭', '2': '𝟮', '3': '𝟯', '4': '𝟰', '5': '𝟱', '6': '𝟲', '7': '𝟳', '8': '𝟴', '9': '𝟵',
    ' ': ' ', '!': '!', ':': ':', '|': '|'
}
def bold(text):
    return ''.join(bold_map.get(char, char) for char in str(text))
import builtins
original_print = print
def print(*args, **kwargs):
    bolded = [bold(a) for a in args]
    original_print(*bolded, **kwargs)
    
import os, io, sys, zipfile, base64, random, shutil, subprocess, tempfile, string, lzma, marshal, autopep8, time, bz2, zlib, gzip
from pathlib import Path
from datetime import datetime
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

def get_bot_token():
    print("\n" + "="*50)
    print("🤖 TELEGRAM BOT SETUP")
    print("="*50)
    token = input("Please enter your Telegram Bot Token: ").strip()
    
    if not token or ":" not in token:
        print("❌ Invalid token format. Please enter a valid bot token.")
        return get_bot_token()
    
    return token

BOT_TOKEN = get_bot_token()
ALLOWED_USERS = []  

def generate_random_suffix(length=10):
    characters = string.ascii_uppercase + string.digits
    return ''.join(str(random.randint(1, 10)) for _ in range(length))

def gw(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def remove_comments(input_file, output_file):
    with open(input_file, 'r') as input_f:
        content = input_f.read()
    
    output_content = ''
    in_comment = False
    i = 0
    
    while i < len(content):
        if content[i:i+2] == '/*':
            in_comment = True
            i += 4
            continue
        elif content[i:i+2] == '*/':
            in_comment = False 
            i += 2
            continue
        if not in_comment:
            output_content += content[i]
        i += 1
    
    with open(output_file, 'w') as output_f:
        output_f.write(output_content)

status_messages = [
    "🔄 Initializing encryption engine...",
    "🔧 Configuring obfuscation layers...",
    "⚙️ Setting up code protection...",
    "📦 Preparing compilation environment...",
    "🔒 Applying security measures...",
    "🚀 Optimizing performance...",
    "🛡️ Building protection shield...",
    "💫 Finalizing encryption process...",
    "🔍 Validating output integrity...",
    "✅ Completing final checks..."
]

def display_status():
    status = random.choice(status_messages)
    print(f"\x1b[1;36m[{datetime.now().strftime('%H:%M:%S')}] {status}")
    time.sleep(random.uniform(0.2, 0.5))

def print_header():
    print("\n" + "="*60)
    print("\x1b[1;95m🤖 Aotpy Encodex ENCRYPTION ENGINE")
    print("\x1b[1;36m🔒 Advanced Python Code Protection")
    print("="*60 + "\x1b[0m\n")

def print_success(message):
    print(f"\x1b[1;92m✅ {message}\x1b[0m")

def print_error(message):
    print(f"\x1b[1;91m❌ {message}\x1b[0m")

def print_info(message):
    print(f"\x1b[1;94mℹ️  {message}\x1b[0m")

def print_warning(message):
    print(f"\x1b[1;93m⚠️  {message}\x1b[0m")

# OPTIMIZED FIRST LAYER
def add_first_layer(code):
    first_layer = '''import time,sys,os
def _aotpy_display():
    print("\\033[96mThis Encoded by - @Aotpy | Channel : ObitoStuffs\\033[0m",flush=True)
    time.sleep(3)
    sys.stdout.write("\\033[1A\\033[2K")
    sys.stdout.flush()
if __name__=="__main__":_aotpy_display()
'''
    return first_layer + "\n" + code

def g(name, file_path):
    w = open(f"m/{name}", "r", encoding="utf-8")
    a = w.read()
    w.close()
    
    # Add first layer here
    a = add_first_layer(a)
    
    a = """
    exec(bytes([35,32,83,111,117,114,99,101,32,71,101,110,101,114,97,116,101,100,32,119,105,116,104,32,68,101,99,111,109,112,121,108,101,43,43,10,35,32,70,105,108,101,58,32,100,101,99,95,68,69,86,73,76,46,112,121,32,40,80,121,116,104,111,110,32,51,46,57,41,10,10,10,35,69,114,114,111,114,32,100,101,99,111,109,112,121,108,105,110,103,32,100,101,99,95,68,69,86,73,76,46,112,121,58,32,118,101,99,116,111,114]).decode())
    import os
    os.system('clear')\n""" + a
    
    print_header()
    print_info("Starting encryption process...")
    display_status()
    
    aa = autopep8.fix_code(a)
    os.remove(f"m/{name}")
    
    with open(f"m/{name}", 'w') as output_f:
        output_f.write(aa)
    
    print_info("Applying code formatting and optimization...")
    display_status()
    
    os.system(f"cython m/{name}")
    name2 = name.replace(".py", ".c")
    
    with open(f"m/{name2}", "r") as f:
        if len(f.read()) < 1000:
            print_error(" compilation failed! Process aborted.")
            exit()
    
    print_info("Compiling Python to C with Cython...")
    display_status()
    
    remove_comments(f"m/{name2}", f"m/{name2}")
    display_status()
    
    name2 = name.replace(".py", "")
    
    # FIXED C CODE FOR PYTHON 3.11+
    c = '''
#ifdef __FreeBSD__
#include <dede.h>
#endif
#if PY_MAJOR_VERSION < 3
int main(int argc, char** argv) {
#elif defined(Win32) || defined(MS_WINDOWS)
int wmain(int argc, wchar_t **argv) {
#else
static int __Pyx_main(int argc, wchar_t **argv) {
#endif
#ifdef __FreeBSD__
    fp_except_t m;
    m = fpgetmask();
    fpsetmask(m & ~FP_X_OFL);
#endif
    #if PY_VERSION_HEX < 0x030B0000
        if (argc && argv)
            Py_SetProgramName(argv[0]);
        Py_Initialize();
        if (argc && argv)
            PySys_SetArgv(argc, argv);
    #else
        PyConfig config;
        PyConfig_InitPythonConfig(&config);
        if (argc && argv) {
            PyStatus status = PyConfig_SetBytesString(&config, &config.program_name, argv[0]);
            if (PyStatus_Exception(status)) {
                PyConfig_Clear(&config);
                return 1;
            }
        }
        Py_InitializeFromConfig(&config);
        PyConfig_Clear(&config);
    #endif
    {
      PyObject* m = NULL;
      __pyx_module_is_main_'''+name2+''' = 1;
      #if PY_MAJOR_VERSION < 3
          init'''+name2+'''();
      #elif CYTHON_PEP489_MULTI_PHASE_INIT
          m = PyInit_'''+name2+'''();
          if (!PyModule_Check(m)) {
              PyModuleDef *mdef = (PyModuleDef *) m;
              PyObject *modname = PyUnicode_FromString("__main__");
              m = NULL;
              if (modname) {
                  m = PyModule_NewObject(modname);
                  Py_DECREF(modname);
                  if (m) PyModule_ExecDef(m, mdef);
              }
          }
      #else
          m = PyInit_'''+name2+'''();
      #endif
      if (PyErr_Occurred()) {
          PyErr_Print();
          #if PY_MAJOR_VERSION < 3
          if (Py_FlushLine()) PyErr_Clear();
          #endif
          return 1;
      }
      Py_XDECREF(m);
    }
#if PY_VERSION_HEX < 0x03060000
    Py_Finalize();
#else
    if (Py_FinalizeEx() < 0)
        return 2;
#endif
    return 0;
}
#if PY_MAJOR_VERSION >= 3 && !defined(Win32) && !defined(MS_WINDOWS)
#include <locale.h>
static wchar_t*
__Pyx_char2wchar(char* arg)
{
    wchar_t *res;
#ifdef HAVE_BROKEN_MBSTOWCS
    size_t argsize = strlen(arg);
#else
    size_t argsize = mbstowcs(NULL, arg, 0);
#endif
    size_t count;
    unsigned char *in;
    wchar_t *out;
#ifdef HAVE_MBRTOWC
    mbstate_t mbs;
#endif
    if (argsize != (size_t)-1) {
        res = (wchar_t *)malloc((argsize+1)*sizeof(wchar_t));
        if (!res)
            goto oom;
        count = mbstowcs(res, arg, argsize+1);
        if (count != (size_t)-1) {
            wchar_t *tmp;
            for (tmp = res; *tmp != 0 &&
                     (*tmp < 0xd800 || *tmp > 0xdfff); tmp++)
                ;
            if (*tmp == 0)
                return res;
        }
        free(res);
    }
#ifdef HAVE_MBRTOWC
    argsize = strlen(arg) + 1;
    res = (wchar_t *)malloc(argsize*sizeof(wchar_t));
    if (!res) goto oom;
    in = (unsigned char*)arg;
    out = res;
    memset(&mbs, 0, sizeof mbs);
    while (argsize) {
        size_t converted = mbrtowc(out, (char*)in, argsize, &mbs);
        if (converted == 0)
            break;
        if (converted == (size_t)-2) {
            fprintf(stderr, "unexpected mbrtowc result -2");
            free(res);
            return NULL;
        }
        if (converted == (size_t)-1) {
            *out++ = 0xdc00 + *in++;
            argsize--;
            memset(&mbs, 0, sizeof mbs);
            continue;
        }
        if (*out >= 0xd800 && *out <= 0xdfff) {
            argsize -= converted;
            while (converted--)
                *out++ = 0xdc00 + *in++;
            continue;
        }
        in += converted;
        argsize -= converted;
        out++;
    }
#else
    res = (wchar_t *)malloc((strlen(arg)+1)*sizeof(wchar_t));
    if (!res) goto oom;
    in = (unsigned char*)arg;
    out = res;
    while(*in)
        if(*in < 128)
            *out++ = *in++;
        else
            *out++ = 0xdc00 + *in++;
    *out = 0;
#endif
    return res;
oom:
    fprintf(stderr, "out of memory");
    return NULL;
}
int
main(int argc, char **argv)
{
    if (!argc) {
        return __Pyx_main(0, NULL);
    }
    else {
        int i, res;
        wchar_t **argv_copy = (wchar_t **)malloc(sizeof(wchar_t*)*argc);
        wchar_t **argv_copy2 = (wchar_t **)malloc(sizeof(wchar_t*)*argc);
        char *oldloc = strdup(setlocale(LC_ALL, NULL));
        if (!argv_copy || !argv_copy2 || !oldloc) {
            fprintf(stderr, "out of memory");
            free(argv_copy);
            free(argv_copy2);
            free(oldloc);
            return 1;
        }
        res = 0;
        setlocale(LC_ALL, "");
        for (i = 0; i < argc; i++) {
            argv_copy2[i] = argv_copy[i] = __Pyx_char2wchar(argv[i]);
            if (!argv_copy[i]) res = 1;
        }
        setlocale(LC_ALL, oldloc);
        free(oldloc);
        if (res == 0)
            res = __Pyx_main(argc, argv_copy);
        for (i = 0; i < argc; i++) {
#if PY_VERSION_HEX < 0x03050000
            free(argv_copy2[i]);
#else
            PyMem_RawFree(argv_copy2[i]);
#endif
        }
        free(argv_copy);
        free(argv_copy2);
        return res;
    }
}
#endif
'''
    
    with open(f"m/{name2}.c", 'r') as input_f:
        co = input_f.read() + c + "\"\"\""
    
    file1 = file_path.replace('.py', '')
    out = f"{file1}-ENC.py"
    
    a=f'''import os,time,sys
PREFIX=sys.prefix
EXECUTE_FILE=".Aotpy/{name2}"
EXPORT_PYTHONHOME="export PYTHONHOME="+sys.prefix
EXPORT_PYTHON_EXECUTABLE="export PYTHON_EXECUTABLE="+sys.executable
RUN="./"+EXECUTE_FILE
if os.path.isfile(EXECUTE_FILE):
    os.system(EXPORT_PYTHONHOME+"&&"+EXPORT_PYTHON_EXECUTABLE+"&&"+RUN)
    exit(0)
C_SOURCE=r"""'''
    
    b=f'''
C_FILE="{name2}.c"
PYTHON_VERSION=".".join(sys.version.split(" ")[0].split(".")[:-1])
COMPILE_CMD=f'gcc -I{{PREFIX}}/include/python{{PYTHON_VERSION}} -o {{EXECUTE_FILE}} {{C_FILE}} -L{{PREFIX}}/lib -lpython{{PYTHON_VERSION}} -lm'
with open(C_FILE,'w')as f:f.write(C_SOURCE)
os.makedirs(os.path.dirname(EXECUTE_FILE),exist_ok=True)
os.system(f"{{EXPORT_PYTHONHOME}} && {{EXPORT_PYTHON_EXECUTABLE}} && {{COMPILE_CMD}} && {{RUN}}")
os.remove(C_FILE)'''
    
    code = a + co + b
    
    if '\x00' in code:
       raise ValueError("The entered code contains zero bytes.")
    
    display_status()
    
    # OPTIMIZED: Reduce multiple marshal/zlib layers
    compiled_code = compile(code, 'Aotpy', 'exec')
    serialized_code = marshal.dumps(compiled_code)
    
    # Single zlib compression
    compressed = zlib.compress(serialized_code, level=9)  # Maximum compression
    
    # Create compact payload
    payload = f'''#@Aotpy Encodex
import zlib,marshal
c=bytes({list(compressed)})
exec(marshal.loads(zlib.decompress(c)))'''
    
    # OPTIMIZED: Direct base64 without intermediate steps
    encoded = base64.b64encode(payload.encode('utf-8')).decode('utf-8')
    
    display_status()
    print_info("Applying optimized  encryption...")
    
    # OPTIMIZED final code - minimal footprint
    final_code = f'''import os, sys, time, base64,tempfile, platform
plat = platform.system().lower()
Aotpy="{encoded}"
e=base64.b64decode(Aotpy).decode()
t=tempfile.gettempdir()
p=os.path.join(t,".Aotpy_payload.py")
os.makedirs(os.path.dirname(p),exist_ok=1)
with open(p,'w')as f:f.write(e)
try:exec(e)
except Exception as ex:print(f"Error:{{ex}}")
finally:
    if os.path.exists(p):os.remove(p)
'''
    
    os.remove(f"m/{name}")
    with open(out, 'w') as output_f:
        output_f.write(final_code)
    
    # Show file size comparison
    original_size = os.path.getsize(file_path)
    encrypted_size = os.path.getsize(out)
    
    print_info(f"Original size: {original_size/1024:.1f} KB")
    print_info(f"Encrypted size: {encrypted_size/1024:.1f} KB")
    
    if encrypted_size > 1024*1024:  # If > 1MB
        print_warning("Warning: Output file is large (>1MB)")
    else:
        print_success("File size optimized successfully!")
    
    return out

def encrypt_file(file_path):
    if not os.path.exists(file_path):
        return None, f"Error: File '{file_path}' not found!"
    
    if not os.path.exists("m/"):
        os.mkdir("m")

    print_header()
    print_info("Starting optimized encryption process...")
    print_info(f"Processing file: {file_path}")
    
    name = file_path.split("/")[-1]
    name2 = gw(2) + ".py"
    shutil.copyfile(file_path, f"m/{name2}")
    
    try:
        output_file = g(name2, file_path)
        
        print_success(f"Encryption completed! Output file: {output_file}")
        
        if os.path.exists('m'):
            shutil.rmtree('m')
        
        return output_file, None
    except Exception as e:
        if os.path.exists('m'):
            shutil.rmtree('m')
        return None, f"Encryption failed: {str(e)}"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    welcome_text = f"""
🤖 *Aotpy Encodex Bot*
Hello {user.first_name}! 👋
I can encrypt your Python files using optimized encryption technology.
*Available Commands:*
/start - Show this welcome message
/help - Get help on how to use the bot
/encrypt - Encrypt a Python file
*Encryption Features:*
*How to use:*
1. Send me a Python (.py) file
2. Or use /encrypt command
3. I'll return the encrypted version
🔒 *Note:* This tool is for educational and security research purposes only.
    """
    await update.message.reply_text(welcome_text, parse_mode='Markdown')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
📖 *How to Use Aotpy Encodex Bot*
*Method 1 - Direct File Upload:*
Simply send me any Python (.py) file and I'll automatically encrypt it.
*Method 2 - Using Command:*
Use /encrypt command and then send the Python file when prompted.
*Requirements:*
- File must have .py extension
- File size should be reasonable
- The bot needs proper permissions
*Encodex Features:*
🔹 Size-optimized encryption (KB range)
⚠️ *Important:*
- Keep backups of original files
- Test encrypted files thoroughly  
- Use responsibly and ethically
- Requires gcc compiler for Encodex
    """
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def encrypt_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    if ALLOWED_USERS and user_id not in ALLOWED_USERS:
        await update.message.reply_text("❌ Sorry, you are not authorized to use this bot.")
        return
    
    context.user_data['waiting_for_file'] = True
    await update.message.reply_text(
        "📤 Please upload the Python file (.py) you want to encrypt with Encodex.\n\n"
        "I'll process it and send back the optimized encrypted version."
    )

async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    if ALLOWED_USERS and user_id not in ALLOWED_USERS:
        await update.message.reply_text("❌ Sorry, you are not authorized to use this bot.")
        return
    
    document = update.message.document
    file_name = document.file_name
    
    if not file_name.endswith('.py'):
        await update.message.reply_text("❌ Please send a Python file with .py extension.")
        return
    
    await update.message.reply_text("📥 Downloading your file...")
    
    try:
        file = await context.bot.get_file(document.file_id)
        download_path = f"temp_{user_id}_{file_name}"
        await file.download_to_drive(download_path)
        
        await update.message.reply_text("🔒 Starting optimized Encodex encryption process...")
        
        encrypted_file_path, error = encrypt_file(download_path)
        
        if error:
            await update.message.reply_text(f"❌ {error}")
            if os.path.exists(download_path):
                os.remove(download_path)
            return
        
        # Get file sizes
        original_size = os.path.getsize(download_path)
        encrypted_size = os.path.getsize(encrypted_file_path)
        
        await update.message.reply_text(
            f"✅ File encrypted successfully!\n"
            f"Original: {original_size/1024:.1f} KB\n"
            f"Encrypted: {encrypted_size/1024:.1f} KB"
        )
        
        with open(encrypted_file_path, 'rb') as f:
            await update.message.reply_document(
                document=f,
                filename=os.path.basename(encrypted_file_path),
                caption=f"🔐 Aotpy Encodex Encrypted File\nSize: {encrypted_size/1024:.1f} KB"
            )
        
        if os.path.exists(download_path):
            os.remove(download_path)
        if os.path.exists(encrypted_file_path):
            os.remove(encrypted_file_path)
            
    except Exception as e:
        await update.message.reply_text(f"❌ Error processing file: {str(e)}")
        temp_files = [f for f in os.listdir('.') if f.startswith(f'temp_{user_id}_')]
        for f in temp_files:
            try:
                os.remove(f)
            except:
                pass

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    if ALLOWED_USERS and user_id not in ALLOWED_USERS:
        await update.message.reply_text("❌ Sorry, you are not authorized to use this bot.")
        return
    
    if context.user_data.get('waiting_for_file'):
        context.user_data['waiting_for_file'] = False
        await update.message.reply_text("❌ Please upload a file, not text. Use /encrypt to try again.")
    else:
        await update.message.reply_text(
            "🤖 Welcome to Aotpy Encodex Encryption Bot!\n\n"
            "Send me a Python file (.py) to encrypt it with Encodex obfuscation, or use /help for more information."
        )

def main():
    if BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
        print("❌ Please set your bot token in the BOT_TOKEN variable!")
        return
    
    application = Application.builder().token(BOT_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("encrypt", encrypt_command))
    application.add_handler(MessageHandler(filters.Document.ALL, handle_document))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print_header()
    print_success("Aotpy Encodex Encryption Bot is running...")
    print_info("Bot is ready to receive files for encryption")
    print("="*60 + "\n")
    
    application.run_polling()

if __name__ == "__main__":
    main()