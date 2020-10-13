while read x 
do
	echo "$x" 1>&2
done

echo "HTTP/1.1 $RANDOM OK"
echo "Date: Wed, 11 Feb 2009 11:20:59 GMT"
echo "Server: Apache"
echo "X-Powered-By: PHP/5.2.4-2ubuntu5wm1"
echo "Last-Modified: Wed, 11 Feb 2009 11:20:59 GMT"
echo "Content-Language: ru"
echo "Content-Type: text/html; charset=utf-8"
echo "Connection: close"
echo ""
echo "<pre>"
date
echo "</pre>"