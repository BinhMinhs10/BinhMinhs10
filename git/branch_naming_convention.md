## Git Branch Naming Convention

## Code flow branches
### Development (dev)
* All new features and bug fixes should be brought to the development branch. Resolving developer codes conflicts should be done as early as here.
### QA/Test (test)
contains all code for QA testing
### Staging (optional)
It contains tested features that the stakeholders wanted to be available either for a demo or a proposal before elevating into the production
### Master (master)
The production branch, if the repository is published, this is the default branch being presented.

## Temporary branches :tada:
### Feature
* Any code changes for a new module or use case should be done on a feature branch
* Examples:
`feature/integrate-swagger` 
`feature/JIRA-1234`
`feature/JIRA-1234_support-dark-theme`
### Bug fix
* If the code changes made from the feature branch were rejected after a release, sprint or demo, any necessary fixes after that should be done on the bugfix branch
* Examples:
`bugfix/more-gray-shades` `bugfix/JIRA-1444_gray-on-blur-fix`
### Experimental
* Any new feature or idea that is not part of a release or a sprint
### Build
* A branch specifically for creating specific build artifacts or for doing code coverage runs
### Release
* A branch for tagging a specific release version
### Merging
* A temporary branch for resolving merge conflicts, usually between the latest development and a feature or Hotfix branch
* Example:
`merge/dev_lombok-refactoring` `merge/combined-device-support`
  
Resource:
* [dev.to](https://dev.to/couchcamote/git-branching-name-convention-cch)