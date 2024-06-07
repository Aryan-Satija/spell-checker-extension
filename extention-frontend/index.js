document.getElementById("spell-submit").addEventListener(
    "click", async()=>{
        const input_div = document.getElementById("spell-search")
        const input_slider = document.getElementById("spell-slider")
        const output_div = document.getElementById("spell-output")
        const searchWord = input_div.value.toLowerCase();
        output_div.innerText = "loading...";
        const response = await fetch(`http://127.0.0.1:5000/spell-check/${searchWord}`);
        const output = await response.json()
        const upper_bound = input_slider.value;
        const len = output.output.length < upper_bound ? output.output.length : upper_bound 
        output_div.innerText = "";
        for(let i = 0; i < len; i += 1){
            const para = document.createElement("p");
            para.textContent = output.output[i][0];
            output_div.appendChild(para);
        }
    }
)