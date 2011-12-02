This is a tiling "window placer" for systems running X. It runs nicely on Ubuntu.
The purpose of the script is to imitate the window placement features of Windows 7,
where you can place windows to the left, right, bottom, top etc using the numpad. I
hear a similar feature is also available in Compiz using the Grid plugin.

Anyway.. By passing a compass point, such as S, N, W or E to tiler.py it will grab
the currently active window and place it in the selected place. In addition to 
the compass points you can also pass F for full screen, which is toggled on and off.

I have bound tiler.py E to <Ctrl><Shift>Right etc.

Here's a guide on adding keyboard bindings in GNOME: http://www.howtogeek.com/howto/ubuntu/assign-custom-shortcut-keys-on-ubuntu-linux/
