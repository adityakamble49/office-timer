rmdir /s /q dist
rmdir /s /q build
rmdir /s /q officetimer.egg-info
python setup.py sdist bdist_wheel
twine upload dist\* -r pypi