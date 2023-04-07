Prompts in the 'prompts.txt' file are separated by new line, and weight with the format:
	
	prompt:[weight]

If no weight is specified, weighting defaults to 1.
A weight of zero eliminates the prompt from the set a runtim.

////////////////////////////////////

TO DO:
- Add GUI. (Will likely use PyQt).
- Save/Load weighted prompt sets.
- Pause/Resume functionality.
	- Commands to adjust interval during pause?
- Save prompt history to file.
- Prompt categories and filtering
	- organise prompts into categories with different rules (eg. defferent intervals etc.).