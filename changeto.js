

function isChinese(str) {
  var entryVal = str;
  var cnChar = entryVal.match(/[^\x00-\x80]/g);
  if (cnChar != null && cnChar.length > 0)
    return true;
  return false;
}

function arraySearch(str) {
  for (var name in Chinese) {
    if (Chinese[name].indexOf(str) != -1) {
      return name;
      break;
    }
  }
  return false;
}

function getPinYin(str, split,uppercase ) {
	split = split || " ";
	uppercase = uppercase || false;
	var l2 = str.length;
	var result = "";
	var reg = new RegExp('[a-zA-Z0-9\-]');
	var val;
	var name;
	for (var i = 0; i < l2; i++) {
		val = str.substr(i, 1);
		if (isChinese(val)) {
		name = arraySearch(val);
		if (reg.test(val)) {
			result += split + val;
		} else if (name !== false) {
			result += split + name;
		}
		} else {
		result += val;
		}
	}
	if(uppercase) result = result.toLowerCase();
	result = result.replace(split,"");
	return result.trim();
}
