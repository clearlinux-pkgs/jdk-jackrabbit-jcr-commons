Name     : jdk-jackrabbit-jcr-commons
Version  : 2.2.5
Release  : 1
URL      : http://repo.maven.apache.org/maven2/org/apache/jackrabbit/jackrabbit-jcr-commons/2.2.5/jackrabbit-jcr-commons-2.2.5.jar
Source0  : http://repo.maven.apache.org/maven2/org/apache/jackrabbit/jackrabbit-jcr-commons/2.2.5/jackrabbit-jcr-commons-2.2.5.jar
Source1  : http://repo.maven.apache.org/maven2/org/apache/jackrabbit/jackrabbit-jcr-commons/2.2.5/jackrabbit-jcr-commons-2.2.5.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-jackrabbit-jcr-commons-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-jackrabbit-jcr-commons package.
Group: Data

%description data
data components for the jdk-jackrabbit-jcr-commons package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/jackrabbit-jcr-commons.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/jackrabbit-jcr-commons.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/jackrabbit-jcr-commons.xml \
%{buildroot}/usr/share/maven-poms/jackrabbit-jcr-commons.pom \
%{buildroot}/usr/share/java/jackrabbit-jcr-commons.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/jackrabbit-jcr-commons.jar
/usr/share/maven-metadata/jackrabbit-jcr-commons.xml
/usr/share/maven-poms/jackrabbit-jcr-commons.pom
