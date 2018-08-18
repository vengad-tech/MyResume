docker build -t vengad-resume .
CID=$(docker create vengad-resume)
docker cp ${CID}:Vengadanathan_Resume.pdf .
docker cp ${CID}:Vengadanathan_Resume.html .
docker rm ${CID}