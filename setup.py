"""Setup script for the package"""

from setuptools import setup


with open("README.md", encoding="UTF-8") as readme_file:
    README = readme_file.read()


def version():
    """Return version string."""

    return "0.1.1"


setup(
    name="whatsapp-media-tools",
    version=version(),
    description="Python scripts to manage WhatsApp media backups for archival purposes",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Alain Girard",
    author_email="alaingirardvd@gmail.com",
    url="https://github.com/Allain18/whatsapp-media-tools",
    license="MIT License",
    keywords="whatsapp, EXIF, image",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Environment :: Console",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6",
    py_modules=["restore_exif", "find_duplicates"],
    install_requires=[
        "piexif>=1.1.3",
    ],
    entry_points={
        "console_scripts":
        [
            "restore-exif = restore_exif:caller",
            "find-duplicates = find_duplicates:caller"
        ]
    }
)
