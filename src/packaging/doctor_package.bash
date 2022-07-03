installation_path=usr/local/bin
src_path=../CommonPython/pyth_04/doctors.py
name=doctor
override_version=$1
architecture=amd64

version=`ls | grep -e "$name_[0-9]" | sort -rn | head -1 | cut -d "_" -f 2 | cut -d "-" -f 1`

version=`awk "BEGIN{print $version + 0.1}"`

if ! [ -z $override_version ]
then
version=$override_version
fi

package_path=$name
package_path+=_$version-1_$architecture

mkdir -p $package_path/DEBIAN
mkdir -p $package_path/$installation_path
mkdir -p tmp

python3 -m PyInstaller --clean --onefile $src_path --workpath tmp --distpath $package_path/$installation_path

rm -rf tmp *.spec

description="Doctors blast with a screwdriver"

echo "Package: $name" > $package_path/DEBIAN/control
echo "Version: $version" >> $package_path/DEBIAN/control
echo "Architecture: $architecture" >> $package_path/DEBIAN/control
echo "Maintainer: Graien" >> $package_path/DEBIAN/control
echo "Description: $description" >> $package_path/DEBIAN/control

dpkg-deb --build --root-owner-group $package_path

rm -rf dist
