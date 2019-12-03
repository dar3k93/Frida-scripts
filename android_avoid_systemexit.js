## run: frida -U -l com.your.package script.js

Java.perform(function () {
  console.log("Step one");
  
	var sysexit = Java.use("java.lang.System");
	sysexit.exit.overload("int").implementation = function(var_0) {
		console.log("system exit bypassing");
	};
});
