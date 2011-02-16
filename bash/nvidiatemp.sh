#!/bin/bash
Version=$(nvidia-settings -q openglversion -t)
Thermal0=$(nvclock -c 1 -T | grep GPU)°C
Thermal1=$(nvclock -c 2 -T | grep GPU)°C
echo "<openbox_pipe_menu>"
echo '<separator label="OpenGL / Version" />'
echo "<item label=\"$Version\" />"
echo  '<separator label="Temperature GPU 0" />'
echo "<item label=\"$Thermal0\" />"
echo  '<separator label="Temperature GPU 1" />'
echo "<item label=\"$Thermal1\" />"

echo "</openbox_pipe_menu>"
