'''
This is a submodule repository which consists of a common functionality which we can include to 
in you project dir A/
    git add submodule path to submod repo
    git add .
    git commit -m 'added sumodule'
    git push origin branchname

    
when the changes made to submodule
in your project repo dir A
    go to cd C---A/C
    git checkout branch of submodule form where we want to pull the changes
    git pull
cd .. --- in A dir
    git submodule update --remote
    git add C(submodule)
    git commit -m 'update submodule to latest changes'
    git push origin main--- branch of your A repo




'''