#!/bin/bash
# Bash Script for install Fsociety tools
# Must run to install tool

clear
echo "
                     /\  \        /\  \        /\  \        /\__\        /\  \    
                    /::\  \      /::\  \      /::\  \      /::|  |      /::\  \   
                   /:/\:\  \    /:/\:\  \    /:/\:\  \    /:|:|  |     /:/\:\  \  
                  /:/  \:\  \  /::\~\:\  \  /:/  \:\  \  /:/|:|__|__  /::\~\:\  \ 
                 /:/__/_\:\__\/:/\:\ \:\__\/:/__/ \:\__\/:/ |::::\__\/:/\:\ \:\__\
                 \:\  /\ \/__/\/_|::\/:/  /\:\  \ /:/  /\/__/~~/:/  /\:\~\:\ \/__/
                  \:\ \:\__\     |:|::/  /  \:\  /:/  /       /:/  /  \:\ \:\__\  
                   \:\/:/  /     |:|\/__/    \:\/:/  /       /:/  /    \:\ \/__/  
                    \::/  /      |:|  |       \::/  /       /:/  /      \:\__\    
                     \/__/        \|__|        \/__/        \/__/        \/__/  
";

sudo chmod +x uninstall

if [ "$PREFIX" = "/data/data/com.termux/files/usr" ]; then
    INSTALL_DIR="$PREFIX/usr/share/doc/fsociety"
    BIN_DIR="$PREFIX/bin/"
    BASH_PATH="$PREFIX/bin/bash"
    TERMUX=true

    pkg install -y git python2
elif [ "$(uname)" = "Darwin" ]; then
    INSTALL_DIR="/usr/local/fsociety"
    BIN_DIR="/usr/local/bin/"
    BASH_PATH="/bin/bash"
    TERMUX=false
else
    INSTALL_DIR="$HOME/.fsociety"
    BIN_DIR="/usr/local/bin/"
    BASH_PATH="/bin/bash"
    TERMUX=false

    sudo apt-get install -y git python2.7
fi

echo "[✔] 检查目录...";
if [ -d "$INSTALL_DIR" ]; then
    echo "[◉] 找到目录grome您要更换吗？ [Y/n]:" ;
    read -r mama
    if [ "$mama" = "y" ]; then
        if [ "$TERMUX" = true ]; then
            rm -rf "$INSTALL_DIR"
            rm "$BIN_DIR/fsociety*"
        else
            sudo rm -rf "$INSTALL_DIR"
            sudo rm "$BIN_DIR/fsociety*"
        fi
    else
        echo "[✘] 如果要安装，必须删除以前的安装[✘]";
        echo "[✘] 安装失败！ [✘]";
        exit
    fi
fi
echo "[✔] 清理旧目录...";
if [ -d "$ETC_DIR/Manisso" ]; then
    echo "$DIR_FOUND_TEXT"
    if [ "$TERMUX" = true ]; then
        rm -rf "$ETC_DIR/Manisso"
    else
        sudo rm -rf "$ETC_DIR/Manisso"
    fi
fi

echo "[✔] 正在安装 ...";
echo "";
git clone --depth=1 https://github.com/Manisso/fsociety "$INSTALL_DIR";
echo "#!$BASH_PATH
python $INSTALL_DIR/fsociety.py" "${1+"$@"}" > "$INSTALL_DIR/fsociety";
chmod +x "$INSTALL_DIR/fsociety";
if [ "$TERMUX" = true ]; then
    cp "$INSTALL_DIR/fsociety" "$BIN_DIR"
    cp "$INSTALL_DIR/fsociety.cfg" "$BIN_DIR"
else
    sudo cp "$INSTALL_DIR/fsociety" "$BIN_DIR"
    sudo cp "$INSTALL_DIR/fsociety.cfg" "$BIN_DIR"
fi
rm "$INSTALL_DIR/fsociety";


if [ -d "$INSTALL_DIR" ] ;
then
    echo "";
    echo "[✔] 工具安装成功! [✔]";
    echo "";
    echo "[✔]====================================================================[✔]";
    echo "[✔]      一切都完成了！！您可以通过键入grome执行工具!       [✔]";
    echo "[✔]====================================================================[✔]";
    echo "";
else
    echo "[✘] 安装失败！ [✘] ";
    exit
fi

