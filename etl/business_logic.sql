# Tax per return
ALTER TABLE quarterlysalestax ADD COLUMN tax_per_return DECIMAL(18,4);
UPDATE quarterlysalestax 
SET tax_per_return = CASE 
    WHEN number_of_returns > 0 THEN computed_tax / number_of_returns
    ELSE 0 END;
    
    
# tax per sales
ALTER TABLE quarterlysalestax ADD COLUMN tax_per_sale_ratio DECIMAL(18, 6);
UPDATE quarterlysalestax
SET tax_per_sale_ratio = CASE
	WHEN taxable_sales > 0 THEN computed_tax / taxable_sales
    ELSE 0 END;
    

#TOP 10 counties by computed tax
SELECT county, SUM(computed_tax) AS total_tax
FROM quarterlysalestax
GROUP BY county
ORDER BY total_tax DESC
LIMIT 10;

#Computed Tax by Quarter
SELECT fiscal_year, quarter_ending, SUM(computed_tax) AS total_tax
FROM quarterlysalestax
GROUP BY fiscal_year, quarter_ending
ORDER BY quarter_ending;

# County Contribution Percentage
SELECT 
    county,
    SUM(computed_tax) AS total_tax,
    ROUND(SUM(computed_tax) * 100 / 
        (SELECT SUM(computed_tax) FROM quarterlysalestax), 2) AS percent_contribution
FROM quarterlysalestax
GROUP BY county
ORDER BY percent_contribution DESC;

-- Get avg and stddev
SELECT 
    AVG(tax_per_sale_ratio) AS mean_val,
    STDDEV(tax_per_sale_ratio) AS std_val
INTO @mean_val, @std_val
FROM quarterlysalestax;

-- Add anomaly flag column
ALTER TABLE quarterlysalestax ADD COLUMN anomaly_flag VARCHAR(10) DEFAULT 'Normal';

-- Update flag
UPDATE quarterlysalestax
SET anomaly_flag = 'Anomaly'
WHERE ABS(tax_per_sale_ratio - @mean_val) > 2 * @std_val;







