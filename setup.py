import setuptools

setuptools.setup(
    name='mac-volume',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/.mute.applescript','scripts/.unmute.applescript','scripts/.volume.applescript','scripts/mute','scripts/unmute','scripts/volume']
)
