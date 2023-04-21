import setuptools, find_packages

setuptools.setup(
    include_package_data=True,
    name='ganesh',
    version =0.0.1,
    description='ganesh python model',
    url = 'https://github.com/Sunitha-Abburu/hybrid',
    author= 'Sunitha',
    packages=setuptools.find_packages(),
    install_requires= ['flask_ngrok','pyngrok==4.1.1','splade','git+https://git@github.com/pinecone-io/pinecone-python-client.git','pandas','pinecone-client' 'openai' 'datasets''flask'],
    classifiers=[
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'],

)