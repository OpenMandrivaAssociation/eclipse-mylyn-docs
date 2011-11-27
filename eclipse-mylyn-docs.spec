%global eclipse_base        %{_libdir}/eclipse
%global install_loc         %{_datadir}/eclipse/dropins
# Taken from update site so we match upstream
#  http://download.eclipse.org/mylyn/archive/3.5.1/v20110422-0200/
%global qualifier           v20110422-0200

Name: eclipse-mylyn-docs
Summary: Eclipse Mylyn documentation tools
Version: 3.5.1
Group:	Development/Java
Release: 3
License: EPL
URL: http://www.eclipse.org/mylyn/docs/

# bash fetch-eclipse-mylyn-docs.sh
Source0: eclipse-mylyn-docs-R_3_5_1-fetched-src.tar.bz2
Source1: fetch-eclipse-mylyn-docs.sh

BuildArch: noarch

BuildRequires: java-devel >= 1.5.0
BuildRequires: eclipse-platform >= 0:3.4.0
BuildRequires: eclipse-pde >= 0:3.4.0
BuildRequires: eclipse-mylyn >= 3.5.0
BuildRequires: eclipse-mylyn-commons >= 3.5.0
BuildRequires: eclipse-mylyn-context >= 3.5.0
Requires: eclipse-mylyn >= 3.5.0
Requires: eclipse-mylyn-commons >= 3.5.0


%description
Enables parsing and display of lightweight markup (wiki text).
Extends the Eclipse Mylyn task editor to create a markup-aware editor.


# eclips-mylyn-docs-wikitext

%package wikitext
Summary: Mylyn WikiText
Requires: eclipse-platform >= 0:3.4.0
Requires: eclipse-mylyn >= 3.5.0
Requires: eclipse-mylyn-commons >= 3.5.0
Requires: eclipse-mylyn-context >= 3.5.0
Provides: eclipse-mylyn-wikitext = %{version}-%{release}
Obsoletes: eclipse-mylyn-wikitext < %{version}-%{release}
Group: Development/Java

%description wikitext
Enables parsing and display of lightweight markup (wiki text).


# eclips-mylyn-docs-htmltext

%package htmltext
Summary: Mylyn HtmlText
Requires: eclipse-platform >= 0:3.4.0
Group: Development/Java

%description htmltext
Enables editing of HTML text.


%prep
%setup -q -n org.eclipse.mylyn.docs


%build
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.mylyn.wikitext_feature \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar \
 -d "mylyn mylyn-commons"
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.mylyn.htmltext \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar


%install
install -d -m 755 %{buildroot}%{_datadir}/eclipse
install -d -m 755 %{buildroot}%{install_loc}/mylyn-docs-wikitext
install -d -m 755 %{buildroot}%{install_loc}/mylyn-docs-htmltext

unzip -q -o -d %{buildroot}%{install_loc}/mylyn-docs-wikitext \
 build/rpmBuild/org.eclipse.mylyn.wikitext_feature.zip
unzip -q -o -d %{buildroot}%{install_loc}/mylyn-docs-htmltext \
 build/rpmBuild/org.eclipse.mylyn.htmltext.zip


# eclips-mylyn-docs-wikitext

%files wikitext
%defattr(-,root,root,-)
%{install_loc}/mylyn-docs-wikitext
%doc org.eclipse.mylyn.wikitext-feature/epl-v10.html
%doc org.eclipse.mylyn.wikitext-feature/license.html


# eclips-mylyn-docs-htmltext

%files htmltext
%defattr(-,root,root,-)
%{install_loc}/mylyn-docs-htmltext
%doc org.eclipse.mylyn.htmltext-feature/epl-v10.html
%doc org.eclipse.mylyn.htmltext-feature/license.html


