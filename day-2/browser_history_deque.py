from collections import deque

# Define the maximum size for the browser history
MAX_HISTORY_SIZE = 5

# Initialize two deque objects for history and forward stack
history = deque(maxlen=MAX_HISTORY_SIZE)
forward_stack = deque() # No maxlen for forward_stack as its size can vary

def display_state():
    """Prints the current state of the browser history and forward stack."""
    print("\n--- Current Browser State ---")
    print(f"History: {list(history)}") # Convert deque to list for cleaner printing
    print(f"Forward Stack: {list(forward_stack)}")
    print("-----------------------------\n")

def add_page(url):
    """
    Adds a new page URL to the history.
    If history size exceeds MAX_HISTORY_SIZE, the oldest page is removed.
    Adding a new page clears the forward stack.
    """
    print(f"Adding page: {url}")
    history.append(url)
    # When a new page is added, the forward history is invalidated
    forward_stack.clear()
    display_state()

def go_back():
    """
    Simulates going back in browser history.
    Removes the last visited page from history and stores it in the forward stack.
    """
    print("Attempting to go back...")
    if len(history) > 1: # Need at least two pages to "go back" from one to another
        # The current page (last one in history) is moved to forward_stack
        last_page = history.pop()
        forward_stack.append(last_page)
        print(f"Backed out from: {last_page}")
    else:
        print("Cannot go back further (history is at its beginning or empty).")
    display_state()

def go_forward():
    """
    Simulates going forward in browser history.
    Restores the most recently backed-out page from the forward stack to history.
    """
    print("Attempting to go forward...")
    if forward_stack:
        # Get the page from the forward stack and add it back to history
        next_page = forward_stack.pop()
        history.append(next_page)
        print(f"Moved forward to: {next_page}")
    else:
        print("No pages to go forward to.")
    display_state()

# --- Demonstrate Browser History System ---

print("--- Initializing Browser History System ---")
display_state()

# Add some pages
add_page("google.com")
add_page("youtube.com")
add_page("github.com")
add_page("stackoverflow.com")
add_page("openai.com")

# History should now be full (5 pages)
# Add another page to demonstrate maxlen behavior
add_page("wikipedia.org") # "google.com" should be removed

# Demonstrate going back
go_back() # wikipedia.org moves to forward_stack
go_back() # openai.com moves to forward_stack
go_back() # stackoverflow.com moves to forward_stack

# Demonstrate going forward
go_forward() # stackoverflow.com moves back to history
go_forward() # openai.com moves back to history

# Add a new page after going back/forward - this should clear forward_stack
add_page("newsite.com")

# Try to go forward (should fail as forward_stack is cleared)
go_forward()

# Add more pages to test maxlen again
add_page("anotherpage.com")
add_page("finalpage.com") # github.com should be removed