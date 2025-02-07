# Career Planner: Smart Career Guidance for LinkedIn Users  

**Rachel Dagan | Inbar Miran | Tamar Dufour Dror**  
**Technion - Israel Institute of Technology**  

![Uploading image.png…]()


## Overview  
Using Machine Learning models, AI, and other statistical tools, we've created a LinkedIn feature based on LinkedIn data and hiring ads that helps LinkedIn users strategically plan their careers and reach their dream jobs.  

## Abstract  
Career planning can be challenging, especially for recent graduates who have a clear long-term goal but struggle to determine the best path to achieve it. Many professionals are unfamiliar with industry dynamics, making it difficult to identify the right opportunities for growth.  

To address this challenge, we introduce **Career Planner**, a LinkedIn feature designed to help users explore career options and set professional goals. By simply entering their dream job into the search bar, users gain access to four essential insights:  

- **Positions on the Way to the Dream Job** – Roles leading to the target position.  
- **People to Connect With** – Suggested networking opportunities with professionals who have successfully followed similar career paths.  
- **Internal Mobility** – Companies that promote and hire internally, based on our internal mobility score.  
- **Skills** – A list of key skills required for the dream job based on Indeed job ads.  

---

## Bright Data User  
For web scraping, we used **Bright Data's** scraping browser services.  
If you want to run the scraping code, we recommend following Bright Data's instructions and creating an account, as explained [here](https://docs.brightdata.com/scraping-automation/scraping-browser/introduction).  

---

## API KEY  
To run the notebook that uses **Gemini**, you need to request an API key (for free!).  

Use this link and create your own API key:  
[Gemini API](https://ai.google.dev/)  

Then, please paste the API key in `Gemini.ipynb` where:  

```python
api_key = 'USE YOUR API KEY'
```

---

## Running the Code  

### Clone this repository:  
```bash
git clone https://github.com/your-repo-link.git](https://github.com/TamarDufour/Career-Planner.git
cd CareerPlannerFolder
```

### Notebook Execution Order  
Some notebooks create datasets that are used in other notebooks.  
All datasets are included in the `datasets` folder.  

In case you want to generate the datasets yourself, we recommend running the notebooks in the following order:  

1. **Scraping**  
   ```bash
   python Main.py
   python txt2csv.py
   ```
   
2. **Career Path Recommendation & People to Connect With**  
   ```bash
   jupyter notebook "Project – Career Path Recommendation & People to Connect With.ipynb"
   ```

3. **Internal Mobility**  
   ```bash
   jupyter notebook "Project – Internal Mobility.ipynb"
   ```

4. **Indeed Requirements Extraction**  
   ```bash
   jupyter notebook "Project – Indeed Requirements Extractions.ipynb"
   ```

5. **Indeed Embeddings**  
   ```bash
   jupyter notebook "Project – Indeed Embeddings.ipynb"
   ```

6. **Indeed Clustering Analysis**  
   ```bash
   jupyter notebook "Project – Indeed after Clustering.ipynb"
   ```

7. **Skills Extraction**  
   ```bash
   jupyter notebook "Project – Skills.ipynb"
   ```

8. **Gemini AI Integration**  
   ```bash
   jupyter notebook "Project – Gemini.ipynb"
   ```

---
