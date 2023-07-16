```
This is a library for automating tasks or testing for Android devices.This library
is based on the Android /bin folder. We use command-line
utilities for some Android events.
```

#Install
```
sudo pip install AutoFi
sudo pip3 install AutoFi
```

# AutoFi - Documentations
<br>
<br>
<h2>-> Class Input</h2>

Input.text( text: string )
```
Pastes the text to the desired location.
```

Input.keyevent( key_code: string )
```
Arguments reserved for KeyEvents.
Keyevents: https://developer.android.com/reference/android/view/KeyEvent
```

Input.tap( x: string, y: string )
```
Click the specific location on the screen.
First and second arguments for coodernadas x and y.
```

Input.swipe( x1: string, y1: string, x2: string, y2: string, duration: string )
```
Slide from coordinates ( x1, y1 ) to ( x2, y2 ) with a specific ( duration )
```

Input.draganddrop( x1: str, y1: str, x2: str, y2: str, duration: str )
```
...
```

Input.press( )
```
...
```

Input.roll( dx: str, dy: str )
```
...
```

<br>
<br>
<h2>-> Class Screen</h2>

Screen.cap( save_cap_path: string )


```
Take a screenshot of the screen, ask for the path and name of the file
followed by its extension.
```

Screen.record( save_record_path: string )
```
starts screen recording, ask for the path and name of the file followed by its extension.
```

Screen.record_stop( )
```
stop screen recording
```


