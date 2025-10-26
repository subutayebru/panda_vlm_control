from setuptools import setup

package_name = 'panda_vlm_control'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Ebru Subutay',
    maintainer_email='subutayebru@gmail.com',
    description='Franka Panda + Gazebo + Vision-Language Model controller',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'your_node = panda_vlm_control.your_node:main',
        ],
    },
)
