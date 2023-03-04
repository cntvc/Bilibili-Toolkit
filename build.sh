tests=tests
src=bilibili_toolkit

function test() {
    poetry run pytest --cov=${src} ${tests} --no-cov-on-fail --cov-report=html
}


function lint(){
    poetry run black ${src} ${tests}
    poetry run isort ${src} ${tests}
    poetry run flake8 ${src} ${tests}
}

if [ "$1" = "test" ]; then
    test
elif [ "$1" = "lint" ]; then
    lint
else
    echo "incorrect arguments."
fi
