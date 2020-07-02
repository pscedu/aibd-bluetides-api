For using the Anaconda environment for the project:

    ssh bridges.psc.edu
    module load anaconda5
    source activate /pylon5/as5pi3p/cosmo/anaconda/cosmo

For running the test suite on the code:

    cd /pylon5/as5pi3p/cosmo/repo/aibd-cosmo/api
    python -m pytest
    

    ======================================= test session starts =======================================
    platform linux -- Python 3.8.3, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
    rootdir: /pylon5/as5pi3p/cosmo/repo/aibd-cosmo/api
    collected 9 items                                                                                 

    test_main.py .........                                                                      [100%]

    ======================================== warnings summary =========================================
    test_main.py::test_get_length
    test_main.py::test_get_length_invalid_haloid
    test_main.py::test_get_length_invalid_typeid
    test_main.py::test_get_index
    test_main.py::test_get_index_invalid_haloid
      /pylon5/as5pi3p/cosmo/anaconda/cosmo/lib/python3.8/site-packages/bigfile/__init__.py:346: DeprecationWarning: BigFile deprecated, use <class 'bigfile.File'> instead
        warnings.warn('%s deprecated, use %s instead' % (name, origin), DeprecationWarning)

    -- Docs: https://docs.pytest.org/en/latest/warnings.html
    ================================== 9 passed, 5 warnings in 0.58s ==================================
