(function () {
	if (typeof AOB === 'undefined') window.AOB = {};

	var UI = AOB.UI = function () {
		this.el = document.getElementById('aob-container');
	}

	UI.prototype.draw_form = function () {
		var go_button = document.getElementById('go');
		go_button.onclick = this.go.bind(this);
	}

	UI.prototype.go = function () {
		var [first, second] = get_form_contents();
		var res = this.query_path(first, second);
	}

	UI.prototype.display_results = function (res_el) {
		var res_container = document.getElementById('res-container');
		res_container.innerHTML = '';
		res_container.appendChild(res_el);
	}

	UI.prototype.query_path = function (first, second) {
		var server_loc = 'http://localhost:5000/path';
		var query_string = `?first=${first}&second=${second}`;

		var request = new XMLHttpRequest();
		request.open('GET', server_loc + query_string);
		request.responseType = 'json';
		request.send();

		request.onload = function () {
			var res = request.response;
			this.display_path_results(res);
		}.bind(this);
	}

	UI.prototype.display_path_results = function (res) {
		var res_el = document.createElement('div');
		res_el.innerHTML = `These two ORCIDs are connected by ${res.length-1} degrees.<br>
			The shortest path is:`;
		res_el.appendChild(elify_arr(res));
		this.display_results(res_el)
	}

	// ---

	function elify_arr(a) {
		var el = document.createElement('ul');
		a.forEach(i => {
			var i_ul = document.createElement('li');
			i_ul.innerText = i;
			el.appendChild(i_ul);
		});
		return el;
	}

	function get_form_contents() {
		var first = document.getElementById('first');
		var second = document.getElementById('second');
		return [first.value, second.value];
	}
})();