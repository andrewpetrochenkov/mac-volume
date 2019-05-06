#!/usr/bin/osascript

on run argv
    if count of argv is 1 then
        set volume output volume (item 1 of argv)
        return
    else
        output volume of (get volume settings)
    end if
end run
