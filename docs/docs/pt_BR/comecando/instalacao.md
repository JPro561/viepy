# Instalação

# Bem-vindo

Welcome to the **Viepy docs**! This Getting Started section will guide you through the basics of Viepy and help you create your first video using the library.

<div class="imp" markdown>
    <p class="imp-title">Important!</p>
    <p>Viepy requires <b>Python 3.11 or newer</b>. Older Python versions are not supported and may cause installation errors or unexpected behavior.</p>
</div>

# Before you begin...

To create videos, **Viepy relies on a few components** that work behind the scenes while you are creating your visualizers.

Before installing Viepy, you need to have the following installed and working on your machine:

- <b>Python 3.11 or newer</b>;
- <b>FFmpeg and FFprobe</b>.

## FFmpeg and FFprobe

Viepy uses **FFmpeg** to process audio and encode the final video. It also uses **FFprobe** to read information about media files.

You need to install both tools and make sure they are available in your system's `PATH`.

### Windows

There are two ways to install FFmpeg on Windows.

#### Winget

First, check if FFmpeg and FFprobe are already installed.

Open Command Prompt or PowerShell and run:

```bash
ffmpeg --version
ffprobe --version
```

If both commands display version information, FFmpeg and FFprobe are already installed and available in your PATH.

If they are not installed, run:

```bash
winget install "FFmpeg (Essentials Build)"
```

After the installation finishes, close and reopen your terminal and run the following commands again:

```bash
ffmpeg --version
ffprobe --version
```

If both commands display version information, FFmpeg and FFprobe are ready to use.

#### Manual installation

If you do not have Winget installed or prefer to install FFmpeg manually, follow these steps.

First, download FFmpeg from the official builds page.

Under the Release Builds section, download:

```
ffmpeg-release-essentials.7z
```

You can also download it [directly here](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.7z).

After downloading the file, extract it.

The extracted folder contains a bin directory. This is the directory that needs to be added to your system's PATH.

For example:

```
C:\ffmpeg\bin
```

To add it to your PATH:

1. Press the Windows key
2. Search for `Environment Variables`
3. Click Edit the system environment variables
4. Click Environment Variables
5. Under System variables, select the `Path` variable
6. Click Edit
7. Click New
8. Add the path to the FFmpeg bin directory
9. Click OK on every window.

After adding FFmpeg to your PATH, close and reopen your terminal.

Finally, verify the installation:

```bash
ffmpeg --version
ffprobe --version
```

If both commands display version information, FFmpeg and FFprobe are correctly installed and ready for Viepy.

# Installing Viepy

Once Python and FFmpeg are installed, you can install Viepy using pip.
<p style="margin-top: 0.75rem;">*<small>Change <code>myViepyProject</code> to the name of the Project you're gonna edit.</small></p>

## Windows

## Powershell

```bash
mkdir myViepyProject
cd myViepyProject
python3 -m venv .venv
.venv\scripts\Activate.ps1
pip install viepy
```

## Command Prompt

```bash
mkdir myViepyProject
cd myViepyProject
python3 -m venv .venv
.venv\scripts\Activate.bat
pip install viepy
```

## Linux and Mac

```bash
mkdir myViepyProject
cd myViepyProject
python -m venv .venv
source .venv/bin/activate
pip install viepy
```

## Test it

Create the `main.py` file with this content:

```python
import viepy
print("Viepy was successfully installed!")
```

And then execute the program: 

```bash
python main.py
```

That's it! You're ready to start **vie**wing with **py**thon!
