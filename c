
if [ -z "$1" ]; then
z=./a
else
z=./b
fi

GTK_DEBUG=all ${z}
