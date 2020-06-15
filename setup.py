from setuptools import setup, find_packages 
  
with open('requirements.txt') as f: 
    requirements = f.readlines() 
  
long_description = '...need to add description' 
  
setup( 
        name ='alhtml', 
        version ='0.4.4', 
        author ='Daniel Weitekamp', 
        author_email ='weitekamp@cmu.edu', 
        url ='https://github.com/apprenticelearner/AL_HTML', 
        description ='Runs Apprentice Learner agents against in tutors.', 
        long_description = long_description, 
        long_description_content_type ="text/markdown", 
        license ='MIT', 
        packages = find_packages(), 
        scripts=['bin/altrain'],
        # entry_points ={ 
            
        # }, 
        classifiers =( 
            "Programming Language :: Python :: 3", 
            "License :: OSI Approved :: MIT License", 
            "Operating System :: OS Independent", 
        ), 
        keywords ='apprentice learner html bridge', 
        install_requires = requirements, 
        zip_safe = False
) 