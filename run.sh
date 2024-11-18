source myenv/bin/activate
python3 -m venv myenv
mkdocs serve

#convert tu docs sang markdown
pip3 install python-docx markdownify

#tao du an moi
mkdocs new kidsafe-guide
cd kidsafe-guide

#
pip3 install python-docx

#
python3 doc2mdbyindex2.py