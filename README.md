# prep tbd

### DO THIS.
# Comments Example:

```
## The main branch.


## Pull out a token based on user name
## This however will fail if a user name contains special chars like `-`, '.' etc.
## We manage personal tokens in a context in circleci called CIRCLE_TOKENS
## To grant a user access, have them generate an api token with their user name and
## then add an context to CIRCLE_TOKENS of the following format:
## CIRCLE_TOKEN_yourusername
TOKEN_NAME=CIRCLE_TOKEN_${CIRCLE_USERNAME} 
CIRCLE_TOKEN=${!TOKEN_NAME}

############################################
## 1. Explenations of logical code chunks.
##
## * It does this
## * it does that
## * then it does this
## * these should be like im walking through the code to somone
## 
############################################

## big chunks can be explained like this. The first chunk is about what its doing in gneral
## 
## Then follow up with a more specific breakdown:
## 1. filter out all main-ci workflows
## 2. group them by commit SHA
## 3. filter out all builds where at least one workflow failed
## 4. sort by queued_at latest-first
## 5. take the commit SHA of the first workflow in the first build
LAST_COMPLETED_BUILD_SHA=$(curl -Ss -u "${CIRCLE_TOKEN}:" "${LAST_COMPLETED_BUILD_URL}" | jq -r 'map(select(.workflows.workflow_name != "main-ci")) | group_by(.vcs_revision) | map(select(all(.status == "success"))) | sort_by(.[0]["queued_at"]) | reverse | .[0][0]["vcs_revision"]')



```


# BASH
use the following whenever possible:
```
#!/bin/bash
set -e
```