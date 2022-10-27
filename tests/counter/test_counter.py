from src.counter import count_ocurrences


def test_counter():
    pass
    resTestPython = count_ocurrences("src/jobs.csv", "python")
    resTestJS = count_ocurrences("src/jobs.csv", "javaScript")
    resTestJest = count_ocurrences("src/jobs.csv", "jest")
    resTestMongoDB = count_ocurrences("src/jobs.csv", "mongodb")
    resTestReact = count_ocurrences("src/jobs.csv", "react")
    assert resTestPython == 1639
    assert resTestJS == 122
    assert resTestJest == 0
    assert resTestMongoDB == 150
    assert resTestReact == 141
