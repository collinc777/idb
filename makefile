.DEFAULT_GOAL := test

FILES :=                              \
    app/models.py                     \
    app/tests.py                     \
    IDB1.html                    \
    IDB1.log                    \
    .gitignore                    \
    makefile                   \
    README.md                    \
    IDB1.pdf                   \
    .travis.yml


check:
	@not_found=0;                                 \
    for i in $(FILES);                            \
    do                                            \
        if [ -e $$i ];                            \
        then                                      \
            echo "$$i found";                     \
        else                                      \
            echo "$$i NOT FOUND";                 \
            not_found=`expr "$$not_found" + "1"`; \
        fi                                        \
    done;                                         \
    if [ $$not_found -ne 0 ];                     \
    then                                          \
        echo "$$not_found failures";              \
        exit 1;                                   \
    fi;                                           \
    echo "success";