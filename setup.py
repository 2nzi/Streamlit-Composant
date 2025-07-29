from setuptools import setup, find_packages

setup(
    name="streamlit-image-carousel",
    version="1.0.0",
    description="Un composant Streamlit moderne pour créer des carrousels d'images interactifs",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Streamlit Image Carousel",
    author_email="contact@example.com",
    url="https://github.com/yourusername/streamlit-image-carousel",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "streamlit>=1.28.0",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
    keywords=["streamlit", "component", "carousel", "image", "interactive", "ui"],
    project_urls={
        "Bug Reports": "https://github.com/yourusername/streamlit-image-carousel/issues",
        "Source": "https://github.com/yourusername/streamlit-image-carousel",
        "Documentation": "https://github.com/yourusername/streamlit-image-carousel#readme",
    },
) 