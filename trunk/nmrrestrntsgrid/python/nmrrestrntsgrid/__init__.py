# Verbosity settings: How much text is printed to stdout/stderr streams
# Reference to it as cing.verbosity if you want to see non-default behavior
verbosityNothing  = 0 # Even errors will be suppressed
verbosityError    = 1 # show only errors
verbosityWarning  = 2 # show errors and warnings
verbosityOutput   = 3 # and regular output DEFAULT
verbosityDetail   = 4 # show more details
verbosityDebug    = 9 # add debugging info (not recommended for casual user)

verbosityDefault  = verbosityOutput
verbosity         = verbosityDefault

#- configure local settings:
#    Create a file localConstants parallel to the setup.py file and add definitions that
#    get imported from the parallel __init__.py code. Just one setting at the moment.
NaNstring = "." # default if not set in localConstants. @UnusedVariable
