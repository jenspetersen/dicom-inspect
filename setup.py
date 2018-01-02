from setuptools import setup

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(name="dicominspect",
      version="0.1",
      description="Inspect DICOM headers",
      long_description=readme,
      url="https://github.com/jenspetersen/dicom-inspect",
      author="Jens Petersen",
      author_email="jens.petersen@dkfz.de",
      license=license,
      packages=["dicominspect"],
      install_requires=["pydicom", "qtpy"],
      entry_points={"gui_scripts": ["dicominspector=dicominspect.run:main"]},
      data_files=[("share/applications", ["data/dicominspector.desktop"])]
)
