

####
# General fields, across multiple pages of the QStack
def jenkinsJobNameFieldValidation(jobNameField):
    """
    job name field is required for all Actions
    """
    pass

####
# Specific to the Create Action
def gitRepoFieldValidation(repoField):
    """
    URL address to the git repo.  If jenkins supports a file path
    to the git repo, that is a current feature request, not yet
    in the works.
    """
    pass

def gitBranchFieldValidation(gitBranchFieldValidation):
    """
    """
    pass

def jenkinsfilePathFieldValidation(jenkinsfileField):
    """
    """
    pass

def jenkinsCredentialsIdFieldValidation(credsIdField):
    """
    """
    pass

####
# Specific to the Run Action
def runParametersFieldValidation(paramsField):
    """
    """
    pass

def tokenBuildFieldValidation(tokenBuildField):
    """
    """
    pass

####
# specific to set-config field
def xmlFilePathFieldValidation(xmlField):
    """
    """
    pass
