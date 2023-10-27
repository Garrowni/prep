
#################################################################
# 1. Set the flask ENV var
#
# * get input from the user 
# * if its relative it needs to be switched to absolute
# * next set that path to the FLASK_APP env var
# * FLASK_APP env is what module should be imported at flask run
##################################################################
$myPath= Resolve-Path (Read-Host "Enter the full path for the app (e.g., ~\Documents\repos\prep\pythonWork\FlaskSQLAlchemyBasic\sqlApp.py'): ")
$env:FLASK_APP = $myPath

#############################
# 2. Create and start a venv
#
# * get the path only by splitting the file off
# * we have to add a "\" because it is removed automatically
# * next we output the path just for visibility sakes.
# * move into the folder we want to venv to live in.
# * on my computer I prefer the venv live with the code
# * start up the venv
#############################
$head, $tail = Split-Path -Path $myPath
$head+="\"
Write-Output "head: $head" 
cd $head
py -3 -m venv .venv
.venv\Scripts\Activate


#############################
# 3. For Flask (Optional)
#
# * If you want flask it will:
# * install Flask
# * run flask
# 
#############################
$installFlask = Read-Host "Do you want to install Flask? (yes/no): "
if ($installFlask -eq "yes") {
    pip install Flask
     Write-Output "Flask Install Completed."
    pip install -U Flask-SQLAlchemy
    flask run
}

