        function clearForm(){
              document.getElementById("form").reset();
          }
        let saveFile = () => {
            // Get the data from each element on the form.
            const title = document.getElementById("title");
            const date = document.getElementById("date");
            const organization = document.getElementById("organization");
            const resume = document.getElementById("resume");
            const letter = document.getElementById("letter");
            const status = document.getElementById("status");
            const comment = document.getElementById("comment");

            // This variable stores all the data.
            let data = "\r Title: " + title.value + " \r\n " + "Date: " + date.value + " \r\n " + "Organisation: "
             + organization.value + " \r\n " + "Link to Resume: " + resume.value + " \r\n " + "Link to Cover letter: "
              + letter.value + " \r\n " + "Status: " + status.value + " \r\n " + "Comment: " + comment.value; //+ "\r\n Last Update: " + newdate;
            //console.log(data); //printing form data into the console
            // Convert the text to BLOB.
            const textToBLOB = new Blob([data], { type: "text/csv" });
            var filename = new Date();
            var month =new Date(); //months from 1-12
            month = month.getMonth();

            var day = new Date();
            var day = day.getUTCDate();

            var year = new Date();
            var year = year.getUTCFullYear();

            newdate = year + "/" + month + "/" + day;
            const sFileName = filename; // The file to save the data.

            let newLink = document.createElement("a");
            newLink.download = new Date();

            if (window.webkitURL != null) {
                newLink.href = window.webkitURL.createObjectURL(textToBLOB);
            } else {
                newLink.href = window.URL.createObjectURL(textToBLOB);
                newLink.style.display = "none";
                document.body.appendChild(newLink);
            }

            newLink.click();
            clearForm();
        };

