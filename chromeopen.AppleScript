on run argv
	tell application "Google Chrome"
		set theUrl to item 1 of argv
		
		if (count every window) = 0 then
			make new window
		end if
		
		set found to false
		set theTabIndex to -1
		repeat with theWindow in every window
			set theTabIndex to 0
			repeat with theTab in every tab of theWindow
				set theTabIndex to theTabIndex + 1
				if theTab's URL = theUrl then
					set found to true
					exit
				end if
			end repeat
			
			if found then
				exit repeat
			end if
		end repeat
		
		if found then
			tell theTab to reload
			set theWindow's active tab index to theTabIndex
			set index of theWindow to 1
		else
			tell window 1 to make new tab with properties {URL:theUrl}
		end if
	end tell
end run