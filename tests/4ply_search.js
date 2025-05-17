d3.csv("covers.csv").then(function(data) {
    var covers = data;
    var button = d3.select("#button");
    var form = d3.select("#form");

    button.on("click", runEnter);
    form.on("submit", runEnter);


    function runEnter() {
        d3.select("tbody").html("");
        d3.event.preventDefault();
        var inputValue = d3.select("#user-input").property("value").toLowerCase(); // Convert input to lowercase
        var filteredMovies = covers.filter(function(cover) {
            // Convert each attribute to lowercase before comparison
            return cover.skater.toLowerCase().includes(inputValue) ||
                cover.trick.toLowerCase().includes(inputValue) ||
                cover.detailer.toLowerCase().includes(inputValue) ||
                cover.obstacle.toLowerCase().includes(inputValue) ||
                cover.soty.toLowerCase().includes(inputValue) ||
                cover.spot.toLowerCase().includes(inputValue) ||
                cover.year.includes(inputValue);
        });

        var output = _.sortBy(filteredMovies, 'year').reverse();
        var resultsCount = filteredMovies.length; // Count the number of search results

        // Display the number of search results
        d3.select("#search-results-count").text("Search results: " + resultsCount);

        // Add the filtered covers to the table
        output.forEach(function(cover) {
            // Add cover to the table
        });

        for (var i = 0; i < filteredMovies.length; i++) {
            // Determine row color based on index
            var rowColorClass = i % 2 === 0 ? 'even-row' : 'odd-row';
            d3.select("tbody").insert("tr").html(
                // "<td>" + (output[i]['issueno'])+ "</td>" +
                "<tr class='" + rowColorClass + "'><td style='display:none;'>" + (output[i]['month']) + "</a>" + "</td>" +
                "<td style='display:none;'>" + (output[i]['year']) + "</td>" +
                "<td style='display:none;'>" + (output[i]['skater']) + "</td>" +
                "<td style='display:none;'>" + (output[i]['trick']) + "</td>" +
                "<td id='info'><div id='info'>" + "Issue: " + (output[i]['month']) + ", " + (output[i]['year']) + "<br>" + "Skater: " + (output[i]['skater']) + "<br>" + "Trick: " + (output[i]['trick']) + "</div></td>" +
                "<td id='coverth'><div id ='covercol'>" + "<img class='tableimg' src='covers/" + (output[i]['month']) + (output[i]['year']) + (output[i]['special']) + ".jpg'" + "</img> " + "</div></td></tr>" +
                "<td style='display:none;'>" + (output[i]['obstacle']) + "</td>" +
                "<td style='display:none;'>" + (output[i]['detailer']) + "</td>" +
                "<td style='display:none;'>" + (output[i]['staircount']) + "</td>" +
                "<td style='display:none;'>" + (output[i]['special']) + "</td>" +
                "<td style='display:none;'>" + (output[i]['spot']) + "</td>" +
                "<td style='display:none;'>" + (output[i]['soty']) + "</td>"
            )
        }

        var table = document.getElementById("tableId");
        var rows = table.getElementsByTagName("tr");
        for (i = 0; i < rows.length; i++) {
            var currentRow = table.rows[i];
            var createClickHandler =
                function(row) {
                    return function() {
                        console.log(currentRow)
                        console.log("bello")

                        var cell = row.getElementsByTagName("td")[0];
                        var id = (row.cells[0].innerHTML + row.cells[1].innerHTML + row.cells[9].innerHTML + ".jpg");
                        var issue = (row.cells[0].innerHTML + ", " + row.cells[1].innerHTML)
                        var skater = (row.cells[2].innerHTML);
                        var trick = (row.cells[3].innerHTML);
                        var obstacle = (row.cells[6].innerHTML);
                        var detailer = (row.cells[7].innerHTML);
                        var staircount = (row.cells[8].innerHTML);
                        var spot = (row.cells[10].innerHTML);
                        var soty = (row.cells[11].innerHTML);

                        document.getElementById("tooltip").style.display = 'block';
                        document.getElementById("innertooltip").innerHTML = ("<img class='ttimg' src='covers/" + id + "' </img> ");
                        document.getElementById("issue").innerHTML = ("issue: " + issue);

                        if ((trick) == "") {
                            document.getElementById("trick").innerHTML = ("");
                        } else {
                            document.getElementById("trick").innerHTML = ("Trick: " + trick);
                        }

                        if ((skater) == "") {
                            document.getElementById("skater").innerHTML = ("");
                        } else {
                            document.getElementById("skater").innerHTML = ("Skater: " + skater);
                        }

                        if ((obstacle) == "") {
                            document.getElementById("obstacle").innerHTML = ("");
                        } else if ((obstacle) == "art") {
                            document.getElementById("obstacle").innerHTML = ("Cover type: Misc");
                        } else {
                            document.getElementById("obstacle").innerHTML = ("Obstacle: " + obstacle);
                        }

                        if ((detailer) == "") {
                            document.getElementById("detailer").innerHTML = ("");
                        } else {
                            document.getElementById("detailer").innerHTML = ("Detailer: " + detailer);
                        }

                        if ((spot) == "") {
                            document.getElementById("spot").innerHTML = ("");
                        } else {
                            document.getElementById("spot").innerHTML = ("Spot: " + spot);
                        }

                        if ((staircount) == "") {
                            document.getElementById("staircount").innerHTML = ("");
                        } else {
                            document.getElementById("staircount").innerHTML = ("Stair count: " + staircount);
                        }

                        if ((location) == "") {
                            document.getElementById("location").innerHTML = ("");
                        } else {
                            document.getElementById("location").innerHTML = ("Location: " + location);
                        }

                        if ((soty) == "") {
                            document.getElementById("soty").innerHTML = ("");
                        } else {
                            document.getElementById("soty").innerHTML = ("*Soty cover");
                        }

                        document.getElementById("tooltip").style.display = 'block';
                        document.getElementById("tooltip").style.opacity = 1;
                    };
                };

            currentRow.onclick = createClickHandler(currentRow);
        }
    };

    window.onload = function closett() {
        document.getElementById("tooltip").style.opacity = 0;
        console.log("tooltip closed");
    }

    function addRowHandlers() {
        var table = document.getElementById("tableId");
        var rows = table.getElementsByTagName("tr");
        for (i = 0; i < rows.length; i++) {
            var currentRow = table.rows[i];
            var createClickHandler =
                function(row) {
                    return function() {
                        console.log(currentRow)
                        var cell = row.getElementsByTagName("td")[0];
                        // var id = cell.innerHTML;
                        alert("id:" + (output[i]['skater']));
                    };
                };

            currentRow.onclick = createClickHandler(currentRow);
        }
    }
    // window.onload = addRowHandlers();
});
